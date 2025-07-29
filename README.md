🚨 BOGONWATCH

Automated tracking of bogon IP lists. Updates run every 4 hours via GitHub Actions to monitor changes in unallocated and reserved IP space.  

---

WHAT ARE BOGONS?

Bogon IP addresses are those that should *never* appear on the public internet:
- ⚠️ Private networks (RFC 1918)
- 🚫 Reserved or special‑use addresses
- ❌ Unallocated IP blocks

---

FILES INCLUDED:
- `bogons_ipv4.txt` — current list of IPv4 bogons  
- `bogons_ipv6.txt` — current list of IPv6 bogons  
- `update_bogons.py` — Python script to fetch and refresh the bogon lists

---

UPDATE SCHEDULE:
- Lists are refreshed automatically every **4 hours** 

DATA SOURCES:
- IPv4: `fullbogons-ipv4.txt`  
- IPv6: `fullbogons-ipv6.txt`

---

WHY USE BOGONWATCH?
- 📊 Track historical changes in bogon allocations over time  
- 🛡️ Useful for network security or anomaly detection  
- ✅ Lightweight, no dependencies, fully automated  
- 🔁 Maintains consistent, timestamped snapshots for audits or analysis
