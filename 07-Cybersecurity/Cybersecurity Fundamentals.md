# Cybersecurity Fundamentals

## Core Concepts

### The CIA Triad
- **Confidentiality** - Ensuring information is accessible only to authorized individuals
- **Integrity** - Maintaining and assuring the accuracy and completeness of data
- **Availability** - Ensuring information and resources are accessible when needed

### Additional Security Properties
- **Authenticity** - Verifying the identity of users, systems, or data
- **Non-repudiation** - Preventing denial of actions or transactions
- **Accountability** - Tracking actions to responsible entities
- **Privacy** - Protecting personal information from unauthorized disclosure

## Threat Landscape

### Types of Threats
- **Malware** - Malicious software (viruses, worms, trojans, ransomware, spyware)
- **Phishing** - Social engineering to obtain sensitive information
- **Denial of Service (DoS/DDoS)** - Overwhelming systems to make them unavailable
- **Man-in-the-Middle (MitM)** - Intercepting and potentially altering communications
- **Zero-day Exploits** - Attacks targeting previously unknown vulnerabilities
- **Advanced Persistent Threats (APTs)** - Prolonged, targeted attacks by sophisticated actors
- **Insider Threats** - Risks from within the organization

### Attack Vectors
- **Network-based** - Exploiting network services and protocols
- **Host-based** - Targeting operating systems and applications
- **Application-based** - Vulnerabilities in software applications
- **Human-based** - Social engineering and phishing
- **Physical** - Direct access to hardware or facilities

## Cryptography

### Symmetric Encryption
- **Block Ciphers** - Encrypt fixed-size blocks (AES, DES, 3DES)
  - Modes of Operation: ECB, CBC, CTR, GCM
  - Padding Schemes: PKCS#7, ANSI X.923
- **Stream Ciphers** - Encrypt bit-by-bit (RC4, Salsa20, ChaCha20)
- **Key Management** - Secure key generation, distribution, storage, and rotation

### Asymmetric Encryption (Public Key Cryptography)
- **RSA** - Based on integer factorization problem
- **Elliptic Curve Cryptography (ECC)** - Based on elliptic curve discrete logarithm
- **Diffie-Hellman Key Exchange** - Secure key establishment over insecure channels
- **Digital Signatures** - Authentication and non-repudiation (RSA, ECDSA, EdDSA)

### Hash Functions
- **Properties** - Deterministic, quick computation, pre-image resistance, collision resistance
- **Common Algorithms** - SHA-256, SHA-3, BLAKE2, MD5 (cryptographically broken)
- **Applications** - Password storage, data integrity, digital signatures, Merkle trees

### Key Derivation Functions
- **PBKDF2** - Password-based key derivation with salt and iterations
- **bcrypt** - Adaptive hash function designed for password hashing
- **scrypt** - Memory-hard key derivation function
- **Argon2** - Winner of Password Hashing Competition (PHC)

## Network Security

### Network Layers & Protocols
- **OSI Model** - 7 layers from Physical to Application
- **TCP/IP Model** - 4 layers (Link, Internet, Transport, Application)
- **Key Protocols**
  - IP/IPv6 - Internet Protocol for addressing and routing
  - TCP/UDP - Transport layer protocols
  - HTTP/HTTPS - Web protocols (HTTPS = HTTP + TLS/SSL)
  - DNS - Domain Name System
  - SSH - Secure Shell for remote access
  - TLS/SSL - Transport Layer Security for encryption
  - IPsec - Network layer security suite

### Firewalls & Network Segmentation
- **Packet Filtering Firewalls** - Stateless inspection based on IP/port
- **Stateful Firewalls** - Track connection state
- **Application-level Gateways (Proxies)** - Inspect application layer traffic
- **Next-Generation Firewalls (NGFW)** - Deep packet inspection, intrusion prevention
- **DMZ (Demilitarized Zone)** - Network segment for public-facing services
- **VLANs & Subnets** - Logical network segmentation
- **Zero Trust Network** - Never trust, always verify principle

### Intrusion Detection & Prevention
- **Network IDS/IPS (NIDS/NIPS)** - Monitor network traffic for threats
- **Host IDS/IPS (HIDS/HIPS)** - Monitor individual systems
- **Signature-based Detection** - Match against known attack patterns
- **Anomaly-based Detection** - Identify deviations from normal behavior
- **Heuristic-based Detection** - Use rules to identify suspicious behavior
- **SIEM (Security Information and Event Management)** - Centralized logging and analysis

## Application Security

### Common Vulnerabilities (OWASP Top 10)
1. **Broken Access Control** - Unauthorized access to functionality/data
2. **Cryptographic Failures** - Weak encryption, sensitive data exposure
3. **Injection** - SQL, NoSQL, OS command, LDAP injection
4. **Insecure Design** - Missing or ineffective security controls
5. **Security Misconfiguration** - Default configs, unnecessary features
6. **Vulnerable Components** - Using outdated/vulnerable libraries
7. **Identification & Authentication Failures** - Weak passwords, session management
8. **Software & Data Integrity Failures** - Untrusted sources, CI/CD issues
9. **Security Logging & Monitoring Failures** - Insufficient detection/response
10. **Server-Side Request Forgery (SSRF)** - Tricking server into making requests

### Secure Development Practices
- **Input Validation** - Validate all input (whitelist where possible)
- **Output Encoding** - Encode data for different contexts (HTML, JS, SQL)
- **Authentication & Authorization** - Strong passwords, MFA, least privilege
- **Session Management** - Secure cookies, timeout, invalidation
- **Error Handling** - Don't leak sensitive information in errors
- **Logging & Monitoring** - Log security events appropriately
- **Dependency Management** - Track and update third-party components
- **Security Testing** - SAST, DAST, penetration testing, fuzzing

### Web Security Specifics
- **Same-Origin Policy** - Restricts cross-origin requests
- **CORS (Cross-Origin Resource Sharing)** - Controlled relaxation of same-origin
- **CSRF Tokens** - Protect against Cross-Site Request Forgery
- **Content Security Policy (CSP)** - Mitigate XSS and data injection attacks
- **HTTP Security Headers** - HSTS, X-Frame-Options, X-Content-Type-Options
- **Secure Cookies** - HttpOnly, Secure, SameSite attributes
- **JSON Web Tokens (JWT)** - Secure token-based authentication

## Endpoint Security

### Operating System Security
- **Patch Management** - Regularly update OS and software
- **Privilege Management** - Least privilege, UAC/sudo, privilege separation
- **Authentication** - Strong passwords, biometrics, multi-factor authentication
- **Authorization** - Access control lists (ACLs), role-based access control (RBAC)
- **Encryption** - Full-disk encryption (BitLocker, FileVault, LUKS)
- **Secure Boot** - Ensure only trusted software runs at startup
- **Antivirus/Anti-malware** - Signature-based and behavioral detection
- **Host-based Firewalls** - Control inbound/outbound connections

### Mobile Device Security
- **Device Encryption** - Protect data at rest
- **Secure Enclave/TEE** - Isolated environment for sensitive operations
- **App Sandboxing** - Isolate applications from each other and system
- **Mobile Device Management (MDM)** - Centralized control of devices
- **App Vetting** - Only install from trusted sources
- **Permissions Management** - Grant minimum necessary permissions
- **Remote Wipe/Locate** - Capabilities for lost/stolen devices

### Cloud Security
- **Shared Responsibility Model** - Cloud provider vs customer responsibilities
- **Identity & Access Management (IAM)** - Control access to cloud resources
- **Data Encryption** - Encrypt data at rest and in transit
- **Network Security** - Virtual networks, security groups, firewalls
- **Monitoring & Logging** - CloudTrail, CloudWatch, audit logs
- **Configuration Management** - Infrastructure as Code (IaC) security
- **Container Security** - Secure images, runtime protection, orchestration
- **Serverless Security** - Function-level permissions, dependency scanning

## Security Operations

### Incident Response
- **Preparation** - Policies, tools, training, communication plans
- **Identification** - Detect and confirm security incidents
- **Containment** - Short-term (isolate) and long-term (temporary fixes)
- **Eradication** - Remove threat artifacts and root causes
- **Recovery** - Restore systems to normal operation, verify
- **Lessons Learned** - Post-incident review, improve defenses
- **Playbooks** - Documented procedures for common incident types

### Security Monitoring
- **Log Collection** - Centralize logs from all sources
- **Log Analysis** - Correlate events, detect anomalies
- **Threat Intelligence** - Feed known IOCs (Indicators of Compromise)
- **Vulnerability Management** - Regular scanning, prioritization, patching
- **Penetration Testing** - Authorized simulated attacks
- **Red Team/Blue Team Exercises** - Adversarial security testing
- **Security Awareness Training** - Educate users about threats and best practices

### Compliance & Governance
- **Frameworks** - ISO 27001, NIST CSF, CIS Controls, SOC 2
- **Regulations** - GDPR, HIPAA, PCI-DSS, CCPA, SOX
- **Risk Assessment** - Identify, analyze, evaluate risks
- **Risk Treatment** - Avoid, transfer, mitigate, accept risks
- **Security Policies** - Acceptable use, access control, incident response
- **Audit & Assessment** - Regular compliance checking
- **Business Continuity** - Disaster recovery planning, backups

## Emerging Trends

### Zero Trust Architecture
- **Principles** - Never trust, always verify; assume breach
- **Components** - Identity verification, device health, least privilege access
- **Microsegmentation** - Granular security controls around workloads
- **Continuous Monitoring** - Real-time assessment of trust

### Artificial Intelligence in Security
- **Threat Detection** - ML for anomaly detection and behavior analysis
- **Automated Response** - AI-driven incident response playbooks
- **Vulnerability Prediction** - Predicting likely vulnerabilities
- **Phishing Detection** - NLP for identifying malicious emails
- **Adversarial ML** - Protecting ML models from manipulation

### IoT & OT Security
- **Device Authentication** - Secure identity for billions of devices
- **Firmware Security** - Secure updates, anti-rollback protection
- **Network Segmentation** - Isolating IoT/OT networks
- **Lightweight Cryptography** - Algorithms for constrained devices
- **Industrial Control Systems (ICS)** - Securing critical infrastructure

### Privacy Enhancing Technologies
- **Homomorphic Encryption** - Compute on encrypted data
- **Zero-Knowledge Proofs** - Prove knowledge without revealing it
- **Secure Multi-party Computation** - Joint computation without sharing inputs
- **Differential Privacy** - Statistical disclosure control
- **Anonymous Communication** - Tor, mixnets, VPNs

---

*Related Notes:*
- [[05-AI-Research/AI Fundamentals]]
- [[06-Math/Mathematics for ML#Information Theory]]
- [[08-Daily/Daily Security Checklist]]
- [[09-Knowledge/Security Case Studies]]

*Last updated: May 14, 2026*