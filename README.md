# building evacuation simulation

final project for cs326 simulation


Pipeline (potential idea)
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
 

In this repository
---
1. `floorparse.py`
2. `preprocess.py`
3. `simulation.py`
4. `main.py`


People
---
- Nick B
- Matthew J
- Aalok S
