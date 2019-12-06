# agent-based building evacuation simulation

final project for cs326 simulation


Usage
---
`python3 evacuate.py`

For help: `python3 evacuate.py -h`


Model
---
We model a floor plan as a 2D grid. A cell neighbors four other cells (top, bottom, left, right).
Each cell has attributes: it can be normal (N), wall (W), bottleneck (B), fire (F), safe zone (S), or people (P).
You can use a GUI program to design input per our specification; 
visit [this repository](https://github.com/aalok-sathe/egress-floorplan-design).

The goal is for as many people to get to the safe zones, away from danger's reach. 
To solve this problem, we represent this 2D grid using a graph with nodes and edges between adjacent nodes (neighbors). 
People may move between adjacent nodes. Each person has their own movement strategy, and implements a move() method that
returns a location. The actual simulation is agnostic of the implementation of this method, allowing for agent-based
modeling experiments. In our case, we consider some baseline strategies: a person will choose to move towards the closest safe
zone with a certain probability, and away from it with the remaining chance. Additionally, agents move at different rates,
congruent to real-world scenario.
A bottleneck is any constricted pathway allowing the passage of only a finite amount of persons in unit time. 
For simplicity, we will consider this limit to be 1. There may be multiple bottlenecks. Exits are ideally bottlenecks, 
otherwise the simulation would not be meaningful or purposeful.

The simulation may run for a max time T, allowing questions such as survival rate; percent people out of danger, 
or until everyone escapes, allowing for studying mean escape time, and time after which most people escape after individual
variability.


Expected directory structure
---
```
./
├── bottleneck.py
├── evacuate.py
├── person.py
│
├── floorplan
│   ├── floorplan.py
│   ├── __init__.py
│   ├── README.md
│   └── requirements.txt
│
├── in
│   └── floor.txt.pkl
│
├── README.md
└── requirements.txt
```


People
---
- Nick B
- Matthew J
- Aalok S



[Scratch work; WIP; to be updated] Pipeline (potential idea)
---
1. Parse a floor plan
2. Preprocess building floor as a graph: locate people spots, danger locs;
    assign numbers of people at each spot (random?); rank exits to each by dist
    (run BFS to find out, this is an unweighted graph) 
3. Simulate: person can move one unit distance in one unit time; look at queues
     at each exit: 'exit' isn't rigorously defined, it's anyhow a person can get
     to the safe zone. Any time there is >1 people at a square, it's a queue.
    SSQ instance at each square as needed. But then how do we make people try
     a different exit when they're stuck? Maybe need queues only at exits, and 
     we could define exits rigorously.
4. Report statistics/questions to think about:
    - Total time
    - Persons outside building after max time T
    - Amount of time taken based on number of people
    - Evenly distributed/clustered people in an area? 
