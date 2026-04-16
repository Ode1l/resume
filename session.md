# WebRTC P2P Session Layer Project Brief

## Summary

I designed and implemented a browser-first WebRTC P2P session layer for turn-based games. The core goal of the project is to separate **transport**, **session orchestration**, **state transitions**, and **game-rule extension points**, so that different games can reuse the same networking and lifecycle infrastructure.

This session layer is built around a **Command Bus + FSM + Observer/Proxy** architecture. Local UI actions and remote peer messages are normalized into the same command pipeline, routed through typed handlers, validated against session state, and then applied to the session store. State changes are observed through an adapter layer and pushed back to the UI, while rule validation and win detection are intentionally exposed as plugin hooks for future game-specific integration.

## Features and Capabilities

- Implemented a lightweight **lockstep session layer** for turn-based games over WebRTC.
- Supported **serverless P2P gameplay** without a dedicated game server.
- Implemented core gameplay actions including **move**, **undo**, and **restart**.
- Added **rule-validation hooks** so game-specific legality checks can be plugged into the session flow.
- Added **offline recovery and synchronization** through reconnect and state sync messages.
- Designed the protocol and state flow to keep both peers' game state consistent during play.

## Architecture Overview

The architecture intentionally divides responsibilities:

- `LocalActionsAPI` is the entry point for local user intent.
- `CommandBus` normalizes all commands and remote messages into one execution path.
- Handlers such as `ready`, `start`, `move`, `undo`, `restart`, and `sync` implement session behavior.
- `State` owns session data, history, pending actions, and the game plugin proxy.
- `SessionFsm` enforces transition legality through `from -> event -> to` rules.
- `NetClient` bridges WebRTC/network transport and the command bus.
- `UINotificationAdapter` and `GameStateObserver` convert internal state changes into UI-facing snapshots and events.
- `IGamePlugin` is the reserved extension point for gameplay rule checks and win conditions.

### Design Notes

- The **bus** is the central integration point. It avoids split logic between “UI code” and “network code”.
- The **session layer** owns protocol legality and pending-request coordination.
- The **FSM** owns deterministic transition rules.
- The **state layer** stores history, turn ownership, pending actions, reconnect context, and plugin access.
- The **proxy/observer path** decouples state mutation from rendering.
- The **game plugin** is intentionally not hard-coded, which keeps the session layer reusable across multiple turn-based games.

## State Machine and Transition Strategy

The project uses a transition-table driven FSM. Each transition is represented as:

```ts
type Transition = {
  from: SessionState;
  event: SessionEvent;
  to: SessionState;
};
```

This model gives the session layer three benefits:

- Every legal state change is explicit and reviewable.
- `canAction()` can reject invalid commands before side effects happen.
- More complex actions such as `START`, `APPROVE`, `REJECT`, and `SYNC_COMPLETE` can still be resolved through helper methods when multiple target states are possible.

### Main States

- `idle / ready / could_start`: lobby and ready-check phase before a match starts.
- `turn / remote_turn`: active gameplay phase, indicating whose turn it is.
- `waiting_approval / approving`: temporary request states for undo or restart.
- `syncing`: reconnect and state recovery phase.
- `offline`: disconnected state.

## Session Envelope and Protocol Design

The session protocol uses a lightweight top-level envelope:

```ts
type SessionMessage = {
  type:
    | 'READY'
    | 'START'
    | 'MOVE'
    | 'UNDO'
    | 'RESTART'
    | 'APPROVE'
    | 'REJECT'
    | 'REJOIN'
    | 'SYNC_REQUEST'
    | 'SYNC_STATE'
    | 'OFFLINE'
    | 'ONLINE'
    | 'GAME_OVER';
  from?: string;
  seq?: number;
  sid?: string;
  turn?: number;
  stateHash?: string;
  payload?: any;
};
```

### Envelope Field Intent

- `type`: command or control category used for routing.
- `from`: sender identity, attached by the network adapter.
- `seq`: reserved for ordered delivery, deduplication, or replay protection.
- `sid`: session identity, used for rejoin and ready validation.
- `turn`: logical move number or turn index.
- `stateHash`: reserved for future desync detection and consistency checks.
- `payload`: flexible action-specific content.

### Protocol Design Principles

- **Single envelope, multiple session actions**: the routing surface stays small while payloads stay flexible.
- **Session-first semantics**: protocol messages describe lifecycle intent, not game rules.
- **Extensible consistency model**: `seq`, `turn`, and `stateHash` create room for future anti-replay and rollback-safe validation.
- **Recovery-aware protocol**: `SYNC_REQUEST` and `SYNC_STATE` allow session restoration after disconnection.
- **Negotiated destructive actions**: `UNDO` and `RESTART` are modeled as requests, finalized only through `APPROVE` or `REJECT`.

### Example Payload Patterns

- `START`: `{ starter: 'sender' | 'receiver' }`
- `UNDO`: `{ count: 1 | 2 }`
- `SYNC_STATE`: `{ history, lastStart, turn, resumeTurn }`
- `GAME_OVER`: `{ winner, turn }`
