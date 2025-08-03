## Suricata Lab Reflection - Qwiklabs

###  🔍 What I Learned
* Learned how to work with Suricata through the Linux command line, and some of its different functions
* Practiced examining Suricata rules and understanding what each part of them means
    * Applied my knowledge of the different parts of rules: Action, Header, and Rule options
* Simulated network traffic that would trigger my custom rule by reading a pcap file and used Suricata to process it
* Practiced reading both types of Suricata log files (eve.json and fast.log)
* Learned how to use the jq command to extract fields from a JSON file and make it more readable


### 🛠️ Commands/Rules Practiced
* Custom Suricata rule:
    * alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; http_method; sid:12345; rev:3;)
* suricata
    * -r
    * -S
    * -k
* cat
* less
* jq
    * -c
    * jq . filepath | less


### 🧠 Reflections
* I loved getting to learn another new security technology and I am continually feeling more confident in my ability to actually protect and monitor systems from a technical side rather than just understanding security principles
* I understand how IDSs and IPSs work in general a lot better now, specifically signature-based ones
* I feel confident both in my ability to configure an IDS like Suricata with custom rules, and in my ability to understand its log output in order to draw conclusions
* I want to explore using different types of actions in my rules. So far I've only used alert actions but I want to try using drop and reject as well, which seem like they can be even more powerful for actually protecting a network from unwanted traffic 