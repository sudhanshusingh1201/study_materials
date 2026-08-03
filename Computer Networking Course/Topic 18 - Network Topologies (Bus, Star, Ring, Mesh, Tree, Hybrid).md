---
title: "Topic 18 - Network Topologies (Bus, Star, Ring, Mesh, Tree, Hybrid)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🕸️ 18. Network Topologies (Bus, Star, Ring, Mesh, Tree, Hybrid)

### 📝 Introduction (Intro)
**Network Topology** batata hai ki ek computer network ke different nodes, links aur devices physically ya logically ek doosre se kaise arranged/connected hain. Topology do types ki hoti hai:
* **Physical Topology:** Network devices physically wires, ports, aur layout se kaise linked hain.
* **Logical Topology:** Data bits internally kis dynamic route se flow karte hain (jo physical arrangement se different ho sakti hai).

#### 🏫 Types of Network Topologies:
1. **Bus Topology:** Isme ek single linear copper cable hoti hai jise **Backbone/Trunk** kehte hain. Saare nodes usi cable se line se connected hote hain. Cable ke dono ends par **Terminator** chips hoti hain jo signals reflection/noise block karti hain.
2. **Star Topology:** Sabse zyada popular setup. Saare devices ek single central node (**Switch or Hub**) se star patterns me judte hain. Traffic routing directly central node se control hoti hai.
3. **Ring Topology:** Har node apne do immediate neighbors se link hokar ek closed circular loop banta hai. Data flow unidirectional hota hai aur control ke liye **Token Passing** system use hota hai.
4. **Mesh Topology:** Isme devices aapas me redundant paths se linked hote hain.
   * **Full Mesh:** Har device baki saare devices se directly separate cables se linked hota hai (total cables = \(\frac{N(N-1)}{2}\)).
   * **Partial Mesh:** Sirf important/critical server nodes aapas me fully connected hote hain, baaki nodes normal local connections rakhte hain.
5. **Tree Topology:** Ye Bus aur Star topologies ka hierarchical blend hai. Isme nodes parent-child hierarchy me linked hote hain, jahan multiple star networks ek single root backbone bus cable se link hote hain.
6. **Hybrid Topology:** Jab do ya do se zyada different topologies (jaise Star aur Ring, ya Star aur Bus) ko mix karke ek customized large network banaya jaye, toh use Hybrid topology bolte hain.

### ➕ Advantages (Fayde)
* **Bus:** Behad sasta, short distances me configuration easy hai, aur minimal cabling lagti hai.
* **Star:** Star networks highly reliable hain. Agar ek client ka connection wire break ho jaye, toh baaki saara network unaffected chalta rehta hai (no impact). New nodes add karna simple hai.
* **Ring:** Data collision (collisions) bilkul zero hote hain kyunki token system se traffic queue control hoti hai. Heavy load me bhi speeds constant rehti hain.
* **Mesh:** Maximum redundancy aur fault tolerance. Agar koi 2 ya 3 cables link toot bhi jayein, data alternate routes se automatic destination tak pahunch jata hai (highly secure and robust).
* **Tree:** segments expand karna aasaan hai (scalability), aur faults segments level par evaluate/troubleshoot karna easy hai.
* **Hybrid:** Custom design capabilities, scalable structure, aur requirements ke according strength options select karne ki freedom.

### ➖ Disadvantages (Nuksan)
* **Bus:** Agar main backbone line toot jaye, toh poora network ek fraction of second me crash (Single point of failure) ho jata hai. Heavy traffic loads me performance weak ho jati hai.
* **Star:** Central switch/hub system hi iska single point of failure hai. Agar switch kharab hua, toh connected saare computers disconnected ho jayenge. Switch and cabling costs extra aati hain.
* **Ring:** Ek single computer ka system crash hona ya intermediate cable cut hona poore ring network loop ko instant shutdown kar deta hai.
* **Mesh:** Cabling cost aur ports usage extremely high hai. Ise manual install, configure, aur manage karna bohot badi complexity (nightmare) hai.
* **Tree:** Agar central main trunk root cable damage ho jaye, toh uski lower sub-branches completely disconnected ho jati hain.
* **Hybrid:** Hardware structures complex ho jate hain, maintenance process expensive ho jata hai, aur multiple interfaces mapping hard hoti hai.

### 📊 Diagram
Ye sabhi common physical topologies ke structures aur linkages ko visual map karta hai:

```mermaid
graph TD
    subgraph Star Topology (Central Control)
        Switch[Central Switch] <--> Star1[PC 1]
        Switch <--> Star2[PC 2]
        Switch <--> Star3[PC 3]
        Switch <--> Star4[PC 4]
    end

    subgraph Ring Topology (Closed Loop)
        R1[Node 1] <--> R2[Node 2] <--> R3[Node 3] <--> R4[Node 4] <--> R1
    end

    subgraph Bus Topology (Linear Backbone)
        T1[Terminator 1] --- BusCable[Backbone Trunk Line] --- T2[Terminator 2]
        BusCable --- B1[PC A]
        BusCable --- B2[PC B]
        BusCable --- B3[PC C]
    end

    subgraph Mesh Topology (Full Redundancy)
        M1((Node A)) <--> M2((Node B))
        M2 <--> M3((Node C))
        M3 <--> M4((Node D))
        M4 <--> M1
        M1 <--> M3
        M2 <--> M4
    end

    subgraph Tree Topology (Hierarchical star-bus)
        Root[Root Backbone Hub] <--> Child1[Switch A]
        Root <--> Child2[Switch B]
        Child1 <--> A1[PC 1]
        Child1 <--> A2[PC 2]
        Child2 <--> B1[PC 3]
        Child2 <--> B2[PC 4]
    end
```

### 💡 Real-world Example (Udaharan)
* **Real-life Metaphors:**
  - **Bus = Single Road Bus Service:** Ek hi common route road hai. Stations line se aate hain. Road damage toh saari buses stuck.
  - **Star = Corporate Cab Dispatch:** Cab driver centers hub se har employee ke flat par jata hai. Ek employee link error se baki employees cabs block nahi hotin.
  - **Ring = Pass the Parcel:** 10 log circle me gift pass kar rahe hain. Ek bhi beech se seat chhod kar bhag jaye toh game thapp.
  - **Mesh = VIP Hotline connections:** Prime Minister and Defense heads ke beech dedicated red telephones (Direct connections) taaki local exchange system drop hone par bhi dynamic lines active rahein.
  - **Tree = School Hierarchy:** Principal -> HODs -> Teachers -> Students.

### 🚀 Application (Kahan use hota hai?)
* **Bus Topology:** Purane coaxial ethernet networks me thinnet structures connection (Legacy).
* **Star Topology:** Aaj ke standard LAN connections (Ghar ka Wi-Fi connection, offices ethernet cabling setups).
* **Ring Topology:** FDDI fiber network backbones, Token Ring systems, aur SONET fiber networks.
* **Mesh Topology:** Core Internet router trunks (BGP routing nodes fully meshed to avoid globally network failures).
* **Tree Topology:** Cable TV distribution frameworks aur large university campus distribution hubs.
* **Hybrid Topology:** Large corporate networks jahan multiple offices (combining campus trees with WAN star structures) integrate hote hain.

---