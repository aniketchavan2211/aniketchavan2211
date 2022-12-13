## Unified Kill Chain(UKC)

### CYCLE 1: In

- Reconnaissance: The attacker performs research on the target using publicly available information.
- Weaponisation: Setting up the needed infrastructure to host the command and control centre (C2) is crucial in executing attacks.
- Delivery: Payloads are malicious instruments delivered to the target through numerous means, such as email phishing and supply chain attacks.
- Social Engineering: The attacker will trick their target into performing untrusted and unsafe action against the payload they just delivered, often making their message appear to come from a trusted in-house source.
- Exploitation: If the attacker finds an existing vulnerability, a software or hardware weakness, in the network assets, they may use this to trigger their payload.
- Persistence: The attacker will leave behind a fallback presence on the network or asset to make sure they have a point of access to their target.
- Defence Evasion: The attacker must remain anonymous throughout their exploits by disabling and avoiding any security defence mechanisms enabled, including deleting evidence of their presence.
- Command & Control: Remember the infrastructure that the attacker prepared? A communication channel between the compromised system and the attacker’s infrastructure is established across the internet.

### Cycle 2: Through

- Pivoting: Remember the system that the attacker may use for persistence? This system will become the attack launchpad for other systems in the network.
- Discovery: The attacker will seek to gather as much information about the compromised system, such as available users and data. Alternatively, they may remotely discover vulnerabilities and assets within the network. This opens the way for the next phase.
- Privilege Escalation: Restricted access prevents the attacker from executing their mission. Therefore, they will seek higher privileges on the compromised systems by exploiting identified vulnerabilities or misconfigurations.
- Execution: With elevated privileges, malicious code may be downloaded and executed to extract sensitive information or cause further havoc on the system.
- Credential Access: Part of the extracted sensitive information would include login credentials stored in the hard disk or memory. This provides the attacker with more firepower for their attacks.
- Lateral Movement: Using the extracted credentials, the attacker may move around different systems or data storages within the network, for example, within a single department.

### Cycle 3:Out

- Collection: After finding the jackpot of data and information, the attacker will seek to aggregate all they need. By doing so, the assets’ confidentiality would be compromised entirely, especially when dealing with trade secrets and financial or personally identifiable information (PII) that is to be secured.
- Exfiltration: The attacker must get his loot out of the network. Various techniques may be used to ensure they have achieved their objectives without triggering suspicion.
- Impact: When compromising the availability or integrity of an asset or information, the attacker will use all the acquired privileges to manipulate, interrupt and sabotage. Imagine the reputation, financial and social damage an organisation would have to recover from.
- Objectives: Attackers may have other goals to achieve that may affect the social or technical landscape that their targets operate within. Defining and understanding these objectives tends to help security teams familiarise themselves with adversarial attack tools and conduct risk assessments to defend their assets
