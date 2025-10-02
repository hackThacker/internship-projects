- [Task 7 :Identify and Remove Suspicious Browser Extensions](#task-7-identify-and-remove-suspicious-browser-extensions)
- [Objective](#objective)
- [Tools](#tools)
- [Deliverables](#deliverables)
- [Guide](#guide)
    - [Access the Extension Manager](#access-the-extension-manager)
    - [Baseline Inventory](#baseline-inventory)
    - [Risk Assessment of Each Extension](#risk-assessment-of-each-extension)
    - [Identify Suspicious or Unused Extensions](#identify-suspicious-or-unused-extensions)
    - [Mitigation Actions](#mitigation-actions)
- [VirusTotal-details ](#virustotal-details-2)
    - [Post-Removal Validation](#post-removal-validation)
- [VirusTotal-behaviour](#virustotal-behaviour31)
    - [Security Research & Awareness](#security-research--awareness)
- [behaviour](#virustotal-behaviour34)
    - [Documentation & Reporting](#documentation--reporting)
- [Outcome](#outcome)



## Task 7 :Identify and Remove Suspicious Browser Extensions

## Objective

Learn to spot and remove potentially harmful browser extensions

## Tools

- Supported web browsers: **Google Chrome, Microsoft Edge, Mozilla Firefox**  
- Access to:  
  - Browser’s **extension/add-ons manager**  
  - Official extension store pages (Chrome Web Store / Firefox Add-ons)  
  - Online threat intelligence sources ( VirusTotal, Hybrid Analysis)  
- Optional: **Endpoint security/antivirus software** for verification  

## Deliverables

List of suspicious extensions found and removed (if any)

## Guide

1.Open your browser’s extension/add-ons manager.

2.Review all installed extensions carefully.

3.Check permissions and reviews for each extension.

4.Identify any unused or suspicious extensions.

5.Remove suspicious or unnecessary extensions.

6.Restart browser and check for performance improvements.

7.Research how malicious extensions can harm users.

8.Document steps taken and extensions removed.

---

### Access the Extension Manager

![extension research](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/extension%20research.png)

- **Brave /Chrome / Edge / Chromium:** Navigate to `chrome://extensions/`.  
- **Firefox:** Navigate to `about:addons`.  
- Ensure the view is set to show **all installed extensions**.  

![extensions](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/extensions%20.png)
---

### Baseline Inventory

- Export or manually record a **complete list of extensions** installed.  
- Include metadata:  
  - Extension **Name**  
  - **Version**  
  - **Publisher/Developer**  
  - **Installation Source** (Web Store, sideloaded, unknown)  
  - **Date Installed**  
![details1](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/details1.png)

---

### Risk Assessment of Each Extension

- **Check Permissions:** Identify if the extension requests high-risk permissions, such as:  
  - `Read and change all data on websites`  
  - `Access to clipboard or keystrokes`  
  - `Modify browser settings (homepage/search)`  
- **Reputation Analysis:**  
  - Verify the **developer identity** and company.  
  - Review extension rating, number of users, and community feedback.  
  - Search threat databases for indicators of compromise (IoCs).  
![permissions](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/permissions.png)

---

### Identify Suspicious or Unused Extensions

- Criteria for suspicion:  
  - Unknown developer or no support website  
  - Recently installed without user knowledge  
  - High-risk permissions without clear justification  
  - Low reviews or negative security reports  
  - Functionality overlap with existing trusted tools  
- Flag both **suspicious** and **unused** extensions for further action.  
![virustotal-crx formate checking](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/virustotal-crx%20formate%20checking%20.png)

---

### Mitigation Actions

- **Option A: Disable (Quarantine Step)**
  - Temporarily disable the extension instead of outright removal.  
  - Observe browser behavior (ads, redirects, performance).  
- **Option B: Removal (Confirmed Malicious/Unnecessary)**  
  - Permanently remove the extension from the browser.  
  - Document removal action with timestamp.  
![installed extension](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/installed%20extension%20.png)

![VirusTotal-details 2](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-details%202.png)
---

### Post-Removal Validation

- Restart the browser to ensure stability.  
- Validate:  
  - No unauthorized homepage or search engine modifications  
  - No unusual background processes remain active  
  - Performance and browsing behavior improved  
![VirusTotal-behaviour3](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-behaviour3.png)

![VirusTotal-behaviour3.1](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-behaviour3.1.png)
---

### Security Research & Awareness

- Research how malicious extensions operate, focusing on:  
  - **Data exfiltration** (harvesting credentials, personal data)  
  - **Ad injection** (redirects, popups, affiliate fraud)  
  - **Cryptojacking** (unauthorized CPU/GPU usage)  
  - **Persistence mechanisms** (reinstalling or hiding in sync profiles)  
- Share findings with security team or include in awareness documentation.  
![VirusTotal-behaviour3.2](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-behaviour3.2.png)

![VirusTotal-behaviour3.3](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-behaviour3.3.png)

![VirusTotal-behaviour3.4](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-behaviour3.4.png)
---

### Documentation & Reporting  

Maintain structured documentation of all actions:  

**Extension Review Log**  

| # | Extension Name | Version  | ID                               | Developer | Risk Level | Action Taken | Date       | size             |
| - | -------------- | -------- | -------------------------------- | --------- | ---------- | ------------ | ---------- | ----------------- |
| 1 | Allow Copy +   | 2.0.0.22 | ajhbdcgfhlhhmocddefknjjkejcfpbnj | pidevex   | medium       | Removed      | 2025-10-02 | 1.2 MB |

![ip traffics](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/ip%20traffics%20.png)

![VirusTotal-File-Relation1](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-7/images/VirusTotal-File-Relation1.png)

## Outcome

- Awareness of browser security risks and managing browser extensions
