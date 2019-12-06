# building evacuation simulation

final project for cs326 simulation


Usage
---
`python3 evacuate.py`

For help: `python3 evacuate.py -h`


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
