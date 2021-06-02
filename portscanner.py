
import streamlit as st
import socket
import termcolor


def scan(target, ports):
	st.text('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		st.write("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


targets = st.text_input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(st.number_input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	st.text(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
