"""Render a role-specific compact resume without modifying the master CV."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/Jiaheng Li Fintech Software Engineering Intern Resume 2026-10-09.pdf'
INK = colors.HexColor('#202225')
ACCENT = colors.HexColor('#a6572e')
BLUE = '#1d4ed8'
BASE = 'https://ode1l.github.io/resume/projects/distributed-systems.html'
styles = {
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.3, leading=12.3, textColor=INK, spaceAfter=4),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.1, leading=10.8, textColor=INK),
    'head': ParagraphStyle('head', fontName='Times-Bold', fontSize=14, leading=17, textColor=ACCENT, spaceBefore=10, spaceAfter=5),
    'name': ParagraphStyle('name', fontName='Times-Bold', fontSize=27, leading=29, textColor=ACCENT),
    'job': ParagraphStyle('job', fontName='Helvetica-Bold', fontSize=9.5, leading=12.4, spaceBefore=5, spaceAfter=3),
}
story = []
def p(text, style='body'):
    return Paragraph(text, styles[style])
def add(text, style='body'):
    story.append(p(text, style))
def link(url, label):
    return f'<a href="{url}" color="{BLUE}"><u>{label}</u></a>'

header = Table([[p('Jiaheng Li', 'name'), p('Auckland, New Zealand<br/>'+link('mailto:odell.lijiaheng@gmail.com','odell.lijiaheng@gmail.com')+'<br/>'+link('https://github.com/Ode1l','GitHub')+' | '+link('https://ode1l.github.io/resume','Portfolio'), 'small')]],colWidths=[295,220])
header.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
story.append(header)
add('Software Engineering Intern | Digital Assets &amp; Fintech', 'job')
add('Open Work Visa to 25 February 2029 | No sponsorship required | Available immediately', 'small')
add('At a Glance','head')
facts = [('<b>Experience:</b> 3 years commercial development','<b>Go:</b> Kademlia DHT implementation'),('<b>Backend:</b> Java/Spring, C#/.NET, REST APIs','<b>Data:</b> SQL, PostgreSQL, Oracle, MyBatis'),('<b>Distributed systems:</b> P2P, multicast, concurrency','<b>Domain:</b> Finance SaaS/ERP; blockchain knowledge')]
t = Table([[p(a,'small'),p(b,'small')] for a,b in facts],colWidths=[265,250])
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,-1),(-1,-1),0.5,colors.HexColor('#d9d3cc'))]))
story.append(t)
add('Software developer with finance-focused SaaS experience and a strong foundation in blockchain principles, peer-to-peer networking and distributed systems. Combines commercial API and database work with a Go DHT thesis and postgraduate protocol implementation.')
add('Relevant Commercial Experience','head')
add('Yonyou Network Technology Co., Ltd. | Junior Backend Developer<br/>Zhengzhou, China | Mar 2022 - Dec 2023','job')
add('Built Java/Spring services, accounting forms and REST integrations for a multi-tenant finance SaaS ERP, supporting workflows across relational databases and enterprise modules.')
add('Implemented a Spring Boot quick-login gateway and a Kafka-backed message-push module handling workloads above 100,000 records through thread-pool processing. Used MyBatis and parallel processing for data transformation and migration.')
add('Skyline Consulting Engineers Limited | Part-time Full-stack Developer<br/>Auckland | Oct 2024 - Dec 2025','job')
add('Translated structural engineers\' calculation workflows into C#/.NET APIs, React/TypeScript UI and PostgreSQL data models. Verified results against analytical benchmarks and worked directly with engineers to clarify requirements and validation rules.')
add('Selected Systems Work','head')
add(link('https://github.com/Ode1l/Go-Kademlia-DHT','Go Kademlia DHT')+' | Undergraduate thesis','job')
add('Implemented all four peer-discovery RPCs, XOR-distance routing and concurrent queries. Integrated the DHT with a torrent-download session; documented peer discovery, packet captures and torrent downloading.')
add(link('https://github.com/Ode1l/Total-Order-Multicast','Total-Order Multicast')+' | C# postgraduate coursework','job')
add('Implemented a multicast protocol and tested consistent delivery ordering across five processes under simulated network delays. Completed and successfully assessed coursework.')
add(link('https://github.com/Ode1l/p2p-lockstep-kit','P2P Lockstep Kit')+' | TypeScript / WebRTC','job')
add('Built reusable peer-to-peer game sessions with deterministic synchronisation, state management and reconnect recovery; supports multiplayer Mahjong.')
add(link('https://github.com/Ode1l/Short-Blockchain-Decentralized-PKI','Blockchain &amp; Decentralized PKI')+' | Postgraduate research','job')
add('Researched lightweight blockchain-based certificate issuance, validation and revocation, including smart-contract concepts and security trade-offs. Unpublished coursework research, not commercial blockchain development.')
add('Education &amp; References','head')
add('<b>Master of Information Technology</b> | University of Auckland | Nov 2025<br/><b>Bachelor of Network Engineering</b> | Henan University | Jun 2022')
add('Former employers are willing to provide references. '+link(BASE,'English project evidence and technical notes')+'.','small')
OUT.parent.mkdir(parents=True,exist_ok=True)
SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=40,leftMargin=40,topMargin=30,bottomMargin=28,title='Jiaheng Li - Fintech Software Engineering Intern',author='Jiaheng Li').build(story)
reader=PdfReader(OUT)
assert len(reader.pages)==1, f'Expected one page, got {len(reader.pages)}'
print(OUT)
print('Pages:',len(reader.pages),'Link annotations:',len(reader.pages[0].get('/Annots',[])))
