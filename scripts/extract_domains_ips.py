#!/usr/bin/env python3
"""
Script to parse M3U playlists, extract domains and IPs, and save them to YAML files.
"""

import re
import os
import yaml
import requests
from urllib.parse import urlparse

# M3U sources - replace with your actual sources
M3U_SOURCES = [
    "https://raw.githubusercontent.com/YueChan/Live/main/Global.m3u",
    "https://raw.githubusercontent.com/YueChan/Live/main/Adult.m3u",
    # Add more M3U sources as needed
]

def is_valid_domain(domain):
    """Check if a string is a valid domain name."""
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    )
    return bool(domain_pattern.match(domain))

def is_valid_ip(ip):
    """Check if a string is a valid IPv4 address."""
    ip_pattern = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    )
    return bool(ip_pattern.match(ip))

def extract_domains_and_ips(m3u_content):
    """Extract domains and IPs from M3U content."""
    domains = set()
    ips = set()
    
    # Regular expression to find URLs in the M3U content
    url_pattern = re.compile(r'https?://([^:/\s]+)')
    
    # Find all matches
    for match in url_pattern.finditer(m3u_content):
        host = match.group(1)
        
        if is_valid_ip(host):
            ips.add(host)
        elif is_valid_domain(host):
            domains.add(host)
    
    return list(domains), list(ips)

def fetch_m3u_content(url):
    """Fetch M3U content from a URL."""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching M3U from {url}: {e}")
        return ""

def main():
    all_domains = set()
    all_ips = set()
    
    for m3u_url in M3U_SOURCES:
        print(f"Fetching M3U from: {m3u_url}")
        m3u_content = fetch_m3u_content(m3u_url)
        
        if m3u_content:
            domains, ips = extract_domains_and_ips(m3u_content)
            all_domains.update(domains)
            all_ips.update(ips)
    
    # Convert sets to sorted lists
    domains_list = sorted(list(all_domains))
    
    # Convert IPs to CIDR format (append /32 to each IP)
    ips_cidr_list = sorted([f"{ip}/32" for ip in all_ips])
    
    # Prepare YAML content
    domains_yaml = {'payload': domains_list}
    ips_yaml = {'payload': ips_cidr_list}
    
    # Write domains to domains.yml
    with open('domains.yml', 'w') as f:
        yaml.dump(domains_yaml, f, default_flow_style=False)
    
    # Write IPs to ips.yml
    with open('ips.yml', 'w') as f:
        yaml.dump(ips_yaml, f, default_flow_style=False)
    
    print(f"Extracted {len(domains_list)} domains and {len(ips_cidr_list)} IPs")

if __name__ == "__main__":
    main()
