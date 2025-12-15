# Controls data organized by category
CONTROLS_BY_CATEGORY = {
    "LT": {
        "nl": [
            {
                "id": "LT-1",
                "name": "Enable threat detection capabilities",
                "description": "Zorg ervoor dat je alle resources monitort op potentiële dreigingen door threat detection capabilities in te schakelen van je cloud service provider, en integreer met je SIEM of andere log analyse tools.",
                "microsoft_solutions": [
                    {
                        "name": "Microsoft Defender for Cloud",
                        "description": "Enable Microsoft Defender for Cloud plans voor alle resource types (Servers, Storage, SQL, Containers, App Service, Key Vault, etc.)",
                        "link": "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction"
                    },
                    {
                        "name": "Microsoft Defender XDR",
                        "description": "Unified security platform die threat detection biedt across endpoints, identities, email, en cloud apps.",
                        "link": "https://learn.microsoft.com/en-us/microsoft-365/security/defender/microsoft-365-defender"
                    },
                    {
                        "name": "Microsoft Sentinel",
                        "description": "Cloud-native SIEM en SOAR oplossing voor intelligente security analytics.",
                        "link": "https://learn.microsoft.com/en-us/azure/sentinel/overview"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Ga naar Azure Portal → Microsoft Defender for Cloud</li>
                    <li>Klik op "Environment settings" en selecteer je subscription</li>
                    <li>Enable de gewenste Defender plans (Servers, Storage, SQL, etc.)</li>
                    <li>Configureer de integratie met Microsoft Sentinel voor SIEM capabilities</li>
                </ol>"""
            },
            {
                "id": "LT-2",
                "name": "Enable threat detection for identity and access management",
                "description": "Detecteer afwijkende of potentieel kwaadaardige identity en access management (IAM) activiteiten door threat detection in te schakelen voor je identity en access management.",
                "microsoft_solutions": [
                    {
                        "name": "Microsoft Entra ID Protection",
                        "description": "Detecteert risico's zoals leaked credentials, anonymous IP login, atypische travel, en meer.",
                        "link": "https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection"
                    },
                    {
                        "name": "Microsoft Defender for Identity",
                        "description": "Cloud-based security oplossing die on-premises Active Directory signalen gebruikt om advanced threats te detecteren.",
                        "link": "https://learn.microsoft.com/en-us/defender-for-identity/what-is"
                    },
                    {
                        "name": "Conditional Access",
                        "description": "Implementeer risk-based conditional access policies die automatisch reageren op gedetecteerde risico's.",
                        "link": "https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Ga naar Microsoft Entra admin center</li>
                    <li>Navigeer naar Protection → Identity Protection</li>
                    <li>Configureer Risk policies voor Sign-in risk en User risk</li>
                    <li>Enable Microsoft Defender for Identity in je Microsoft 365 Defender portal</li>
                </ol>"""
            },
            {
                "id": "LT-3",
                "name": "Enable logging for security investigation",
                "description": "Zorg ervoor dat je de nodige logging inschakelt om security investigations te ondersteunen wanneer een security incident optreedt.",
                "microsoft_solutions": [
                    {
                        "name": "Azure Monitor Logs (Log Analytics)",
                        "description": "Centrale logging oplossing voor het verzamelen en analyseren van logs uit Azure resources.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview"
                    },
                    {
                        "name": "Diagnostic Settings",
                        "description": "Configureer diagnostic settings voor Azure resources om logs te sturen naar Log Analytics, Storage, of Event Hubs.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings"
                    },
                    {
                        "name": "Microsoft Entra Audit Logs",
                        "description": "Audit logs voor alle identity-gerelateerde activiteiten in Microsoft Entra ID.",
                        "link": "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs"
                    },
                    {
                        "name": "Activity Logs",
                        "description": "Azure Activity Logs voor subscription-level events en resource operations.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Maak een Log Analytics Workspace aan in Azure Portal</li>
                    <li>Configureer Diagnostic Settings voor elke Azure resource</li>
                    <li>Stuur logs naar de centrale Log Analytics Workspace</li>
                    <li>Enable Microsoft Entra diagnostic settings voor identity logs</li>
                </ol>"""
            },
            {
                "id": "LT-4",
                "name": "Enable network logging for security investigation",
                "description": "Schakel logging in van je network resources om security investigations te ondersteunen nadat een security incident heeft plaatsgevonden.",
                "microsoft_solutions": [
                    {
                        "name": "NSG Flow Logs",
                        "description": "Log network traffic die door Network Security Groups stroomt voor analyse en forensics.",
                        "link": "https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview"
                    },
                    {
                        "name": "Azure Firewall Logs",
                        "description": "Applicatie en netwerk regel logs van Azure Firewall voor threat investigation.",
                        "link": "https://learn.microsoft.com/en-us/azure/firewall/logs-and-metrics"
                    },
                    {
                        "name": "Traffic Analytics",
                        "description": "Visualiseer network traffic patterns en identificeer security threats.",
                        "link": "https://learn.microsoft.com/en-us/azure/network-watcher/traffic-analytics"
                    },
                    {
                        "name": "Azure DDoS Protection Logs",
                        "description": "Logs en metrics voor DDoS attacks en mitigation.",
                        "link": "https://learn.microsoft.com/en-us/azure/ddos-protection/diagnostic-logging"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Enable NSG Flow Logs via Network Watcher</li>
                    <li>Configureer Azure Firewall diagnostic settings</li>
                    <li>Enable Traffic Analytics voor visualisatie</li>
                    <li>Stuur alle network logs naar je centrale Log Analytics Workspace</li>
                </ol>"""
            },
            {
                "id": "LT-5",
                "name": "Centralize security log management and analysis",
                "description": "Centraliseer logging opslag en analyse om correlatie, investigation, en reporting mogelijk te maken.",
                "microsoft_solutions": [
                    {
                        "name": "Microsoft Sentinel",
                        "description": "Centraliseer alle security logs in Sentinel voor correlatie, hunting, en incident response.",
                        "link": "https://learn.microsoft.com/en-us/azure/sentinel/overview"
                    },
                    {
                        "name": "Log Analytics Workspace",
                        "description": "Centrale workspace voor het verzamelen van logs uit meerdere bronnen.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview"
                    },
                    {
                        "name": "Data Connectors",
                        "description": "Gebruik Sentinel data connectors om logs te verzamelen van Microsoft en third-party bronnen.",
                        "link": "https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Deploy Microsoft Sentinel op je Log Analytics Workspace</li>
                    <li>Configureer Data Connectors voor alle log sources</li>
                    <li>Maak Analytics Rules voor threat detection</li>
                    <li>Configureer Workbooks voor visualisatie en reporting</li>
                </ol>"""
            },
            {
                "id": "LT-6",
                "name": "Configure log storage retention",
                "description": "Stel log retention policies in om ervoor te zorgen dat logs beschikbaar zijn voor security investigation en compliance requirements.",
                "microsoft_solutions": [
                    {
                        "name": "Log Analytics Retention",
                        "description": "Configureer retention policies in Log Analytics (standaard 30 dagen, max 730 dagen interactief).",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive"
                    },
                    {
                        "name": "Archive to Storage Account",
                        "description": "Archiveer logs naar Azure Storage voor lange termijn retentie tegen lagere kosten.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/resource-logs#send-to-azure-storage"
                    },
                    {
                        "name": "Immutable Storage",
                        "description": "Gebruik immutable blob storage voor compliance en data protection.",
                        "link": "https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Configureer Log Analytics retention (30-730 dagen)</li>
                    <li>Setup archive policies voor lange termijn opslag</li>
                    <li>Gebruik Azure Storage met immutable policies voor compliance</li>
                    <li>Documenteer retention policies conform je compliance requirements</li>
                </ol>"""
            },
            {
                "id": "LT-7",
                "name": "Use approved time synchronization sources",
                "description": "Gebruik goedgekeurde time synchronization bronnen om accurate timestamps voor logging events te garanderen.",
                "microsoft_solutions": [
                    {
                        "name": "Azure Time Sync",
                        "description": "Azure VMs synchroniseren automatisch met Microsoft time servers via Windows Time service of NTP.",
                        "link": "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/time-sync"
                    },
                    {
                        "name": "Windows Time Service",
                        "description": "Configureer Windows Time Service voor accurate time synchronization in hybrid scenarios.",
                        "link": "https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-top"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Azure VMs gebruiken automatisch Microsoft time servers</li>
                    <li>Verifieer NTP configuratie op Linux VMs</li>
                    <li>Configureer Windows Time Service voor hybrid scenarios</li>
                    <li>Monitor time sync status via Azure Monitor</li>
                </ol>"""
            }
        ],
        "en": [
            {
                "id": "LT-1",
                "name": "Enable threat detection capabilities",
                "description": "Ensure you are monitoring all resources for potential threats by enabling threat detection capabilities from your cloud service provider, as well as integrating with your SIEM, or other log analysis tools.",
                "microsoft_solutions": [
                    {
                        "name": "Microsoft Defender for Cloud",
                        "description": "Enable Microsoft Defender for Cloud plans for all resource types (Servers, Storage, SQL, Containers, App Service, Key Vault, etc.)",
                        "link": "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction"
                    },
                    {
                        "name": "Microsoft Defender XDR",
                        "description": "Unified security platform that provides threat detection across endpoints, identities, email, and cloud apps.",
                        "link": "https://learn.microsoft.com/en-us/microsoft-365/security/defender/microsoft-365-defender"
                    },
                    {
                        "name": "Microsoft Sentinel",
                        "description": "Cloud-native SIEM and SOAR solution for intelligent security analytics.",
                        "link": "https://learn.microsoft.com/en-us/azure/sentinel/overview"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Go to Azure Portal → Microsoft Defender for Cloud</li>
                    <li>Click on "Environment settings" and select your subscription</li>
                    <li>Enable the desired Defender plans (Servers, Storage, SQL, etc.)</li>
                    <li>Configure integration with Microsoft Sentinel for SIEM capabilities</li>
                </ol>"""
            },
            {
                "id": "LT-2",
                "name": "Enable threat detection for identity and access management",
                "description": "Detect anomalous or potentially malicious identity and access management (IAM) activities by enabling threat detection for your identity and access management.",
                "microsoft_solutions": [
                    {
                        "name": "Microsoft Entra ID Protection",
                        "description": "Detects risks such as leaked credentials, anonymous IP login, atypical travel, and more.",
                        "link": "https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection"
                    },
                    {
                        "name": "Microsoft Defender for Identity",
                        "description": "Cloud-based security solution that uses on-premises Active Directory signals to detect advanced threats.",
                        "link": "https://learn.microsoft.com/en-us/defender-for-identity/what-is"
                    },
                    {
                        "name": "Conditional Access",
                        "description": "Implement risk-based conditional access policies that automatically respond to detected risks.",
                        "link": "https://learn.microsoft.com/en-us/entra/identity/conditional-access/overview"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Go to Microsoft Entra admin center</li>
                    <li>Navigate to Protection → Identity Protection</li>
                    <li>Configure Risk policies for Sign-in risk and User risk</li>
                    <li>Enable Microsoft Defender for Identity in your Microsoft 365 Defender portal</li>
                </ol>"""
            },
            {
                "id": "LT-3",
                "name": "Enable logging for security investigation",
                "description": "Ensure that you enable necessary logging to support security investigations when a security incident occurs.",
                "microsoft_solutions": [
                    {
                        "name": "Azure Monitor Logs (Log Analytics)",
                        "description": "Central logging solution for collecting and analyzing logs from Azure resources.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview"
                    },
                    {
                        "name": "Diagnostic Settings",
                        "description": "Configure diagnostic settings for Azure resources to send logs to Log Analytics, Storage, or Event Hubs.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings"
                    },
                    {
                        "name": "Microsoft Entra Audit Logs",
                        "description": "Audit logs for all identity-related activities in Microsoft Entra ID.",
                        "link": "https://learn.microsoft.com/en-us/entra/identity/monitoring-health/concept-audit-logs"
                    },
                    {
                        "name": "Activity Logs",
                        "description": "Azure Activity Logs for subscription-level events and resource operations.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Create a Log Analytics Workspace in Azure Portal</li>
                    <li>Configure Diagnostic Settings for each Azure resource</li>
                    <li>Send logs to the central Log Analytics Workspace</li>
                    <li>Enable Microsoft Entra diagnostic settings for identity logs</li>
                </ol>"""
            },
            {
                "id": "LT-4",
                "name": "Enable network logging for security investigation",
                "description": "Enable logging of your network resources to support security investigations after a security incident occurs.",
                "microsoft_solutions": [
                    {
                        "name": "NSG Flow Logs",
                        "description": "Log network traffic flowing through Network Security Groups for analysis and forensics.",
                        "link": "https://learn.microsoft.com/en-us/azure/network-watcher/nsg-flow-logs-overview"
                    },
                    {
                        "name": "Azure Firewall Logs",
                        "description": "Application and network rule logs from Azure Firewall for threat investigation.",
                        "link": "https://learn.microsoft.com/en-us/azure/firewall/logs-and-metrics"
                    },
                    {
                        "name": "Traffic Analytics",
                        "description": "Visualize network traffic patterns and identify security threats.",
                        "link": "https://learn.microsoft.com/en-us/azure/network-watcher/traffic-analytics"
                    },
                    {
                        "name": "Azure DDoS Protection Logs",
                        "description": "Logs and metrics for DDoS attacks and mitigation.",
                        "link": "https://learn.microsoft.com/en-us/azure/ddos-protection/diagnostic-logging"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Enable NSG Flow Logs via Network Watcher</li>
                    <li>Configure Azure Firewall diagnostic settings</li>
                    <li>Enable Traffic Analytics for visualization</li>
                    <li>Send all network logs to your central Log Analytics Workspace</li>
                </ol>"""
            },
            {
                "id": "LT-5",
                "name": "Centralize security log management and analysis",
                "description": "Centralize logging storage and analysis to enable correlation, investigation, and reporting.",
                "microsoft_solutions": [
                    {
                        "name": "Microsoft Sentinel",
                        "description": "Centralize all security logs in Sentinel for correlation, hunting, and incident response.",
                        "link": "https://learn.microsoft.com/en-us/azure/sentinel/overview"
                    },
                    {
                        "name": "Log Analytics Workspace",
                        "description": "Central workspace for collecting logs from multiple sources.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-workspace-overview"
                    },
                    {
                        "name": "Data Connectors",
                        "description": "Use Sentinel data connectors to collect logs from Microsoft and third-party sources.",
                        "link": "https://learn.microsoft.com/en-us/azure/sentinel/connect-data-sources"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Deploy Microsoft Sentinel on your Log Analytics Workspace</li>
                    <li>Configure Data Connectors for all log sources</li>
                    <li>Create Analytics Rules for threat detection</li>
                    <li>Configure Workbooks for visualization and reporting</li>
                </ol>"""
            },
            {
                "id": "LT-6",
                "name": "Configure log storage retention",
                "description": "Establish log retention policies to ensure logs are available for security investigation and compliance requirements.",
                "microsoft_solutions": [
                    {
                        "name": "Log Analytics Retention",
                        "description": "Configure retention policies in Log Analytics (default 30 days, max 730 days interactive).",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive"
                    },
                    {
                        "name": "Archive to Storage Account",
                        "description": "Archive logs to Azure Storage for long-term retention at lower cost.",
                        "link": "https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/resource-logs#send-to-azure-storage"
                    },
                    {
                        "name": "Immutable Storage",
                        "description": "Use immutable blob storage for compliance and data protection.",
                        "link": "https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Configure Log Analytics retention (30-730 days)</li>
                    <li>Setup archive policies for long-term storage</li>
                    <li>Use Azure Storage with immutable policies for compliance</li>
                    <li>Document retention policies according to your compliance requirements</li>
                </ol>"""
            },
            {
                "id": "LT-7",
                "name": "Use approved time synchronization sources",
                "description": "Use approved time synchronization sources to ensure accurate timestamps for logging events.",
                "microsoft_solutions": [
                    {
                        "name": "Azure Time Sync",
                        "description": "Azure VMs automatically synchronize with Microsoft time servers via Windows Time service or NTP.",
                        "link": "https://learn.microsoft.com/en-us/azure/virtual-machines/linux/time-sync"
                    },
                    {
                        "name": "Windows Time Service",
                        "description": "Configure Windows Time Service for accurate time synchronization in hybrid scenarios.",
                        "link": "https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-top"
                    }
                ],
                "implementation_steps": """<ol>
                    <li>Azure VMs automatically use Microsoft time servers</li>
                    <li>Verify NTP configuration on Linux VMs</li>
                    <li>Configure Windows Time Service for hybrid scenarios</li>
                    <li>Monitor time sync status via Azure Monitor</li>
                </ol>"""
            }
        ]
    },
    # Placeholder for other categories - will show "Coming Soon"
    "NS": {"nl": [], "en": []},
    "IM": {"nl": [], "en": []},
    "PA": {"nl": [], "en": []},
    "DP": {"nl": [], "en": []},
    "AM": {"nl": [], "en": []},
    "IR": {"nl": [], "en": []},
    "PV": {"nl": [], "en": []},
    "ES": {"nl": [], "en": []},
    "BR": {"nl": [], "en": []},
    "DS": {"nl": [], "en": []},
    "AI": {"nl": [], "en": []}
}

def get_all_controls(category_id, lang='nl'):
    category_data = CONTROLS_BY_CATEGORY.get(category_id.upper(), {})
    return category_data.get(lang, category_data.get('nl', []))

def get_control_by_id(category_id, control_id, lang='nl'):
    controls = get_all_controls(category_id, lang)
    for control in controls:
        if control["id"].upper() == control_id.upper():
            return control
    return None
