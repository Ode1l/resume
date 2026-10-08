# Distributed Systems and Blockchain Foundations

Jiaheng Li | Selected academic and personal engineering work

These notes distinguish implemented software from coursework research. Original reports are available on request. Academic work was not presented as peer-reviewed publication or commercial blockchain development.

## Go Kademlia DHT - Undergraduate Thesis

**Purpose:** Discover peers and resources without a central directory.

**Implementation:** Implemented PING, FIND_NODE, GET_PEERS and ANNOUNCE_PEER in Go, with XOR-distance routing, node discovery, concurrent queries using goroutines, and a download-session integration supporting torrent downloading. The thesis describes configuration, routing and peer-management logic.

**Evidence:** The thesis documents peer-query results, Wireshark packet captures and an Ubuntu torrent download using the DHT integrated into a third-party download tool. The DHT implementation and the reused download components are distinct contributions.

**Scope:** Undergraduate software implementation, not a claim to have independently implemented every part of BitTorrent or verified universal client interoperability. The original thesis is in Chinese; its title translates to *Design and Development of the Kademlia Network Protocol Using Go*. Source availability and a reproducible build have not yet been verified for this portfolio.

## Total-Order Multicast - Postgraduate Coursework

**Purpose:** Make participating processes deliver multicast messages in the same order despite different network delays.

**Implementation:** Implemented a total-order multicast protocol in C#. Five middleware processes exchange messages and ordering timestamps; a separate network simulator introduces configured delays. The code includes TCP communication, logical clocks, timestamp agreement and deterministic ordering.

**Evidence:** The application displays sent, received and deliverable messages to check order across processes. Completed and assessed coursework; the author confirms the assignment was graded successfully. Original code and report are retained locally.

**Scope:** A coursework protocol implementation and ordering test harness, not a production consensus service. The archived programs use Windows Forms and a Windows batch launcher. They have not been rerun as part of this documentation update; no new claims about fault tolerance, throughput or exhaustive correctness are made.

## P2P Lockstep Kit - Personal Project

**Purpose:** Provide reusable peer-to-peer sessions for browser games.

**Implementation:** TypeScript and WebRTC, deterministic synchronisation, session state management, reconnect recovery and multiplayer Mahjong support.

**Evidence:** [Source repository](https://github.com/Ode1l/p2p-lockstep-kit) and [live Mahjong](https://mahjong.jiahengli.xyz).

**Scope:** Game networking and state synchronisation, not blockchain consensus.

## Blockchain-Based Decentralized PKI - Postgraduate Research Report

**Title:** *Using Short Blockchain Systems as Decentralized PKI Infrastructure*.

**Contribution:** Reviewed decentralized trust and proposed a lightweight blockchain-based certificate-management design covering issuance, validation, revocation and smart-contract automation. Discussed resource constraints, security assumptions and deployment trade-offs.

**Evidence:** An unpublished postgraduate coursework report, available on request. The focus is PKI and certificate lifecycle management, not primarily DNS.

**Scope:** Research and proposed architecture, not a deployed smart-contract product, completed security audit or measured production outcome. Security benefits described in the proposal depend on its assumptions and are not independently established guarantees.

## ChessServer - Native C# HTTP Server

**Purpose:** Understand HTTP server behaviour below a web framework.

**Implementation:** Built an HTTP/1.1 server using C# Thread and Socket APIs, including TCP connection handling, request parsing, keep-alive, static/binary responses and multiplayer chess state.

**Evidence:** [Source repository](https://github.com/Ode1l/ChessServer).

**Scope:** An academic systems-programming project. A current clean build and full HTTP compliance have not been reverified for these notes; there is no claim of ongoing maintenance or production hardening.
