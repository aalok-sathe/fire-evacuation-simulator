# agent-based building evacuation simulation

this simple simulation program simulates a moving danger situation (e.g., fire) 
and people in a confined space trying to escape away from danger to get to safe zone(s).
additional constraints are modeled as queues, where a limited number of people can pass at once.

final project for [cs326: 'simulation'](http://cs.richmond.edu/courses/index.html)

see it in action!

![action](https://i.imgur.com/JsQBlWi.png)

Usage
---
```
usage: evacuate.py [-h] [-i INPUT] [-n NUMPEOPLE] [-r RANDOM_STATE]
                   [-t MAX_TIME] [-f] [-g] [-v] [-d FIRE_RATE]
                   [-b BOTTLENECK_DELAY] [-a ANIMATION_DELAY]

optional arguments:
  -h, --help            show this help message and exit
  
  -i INPUT, --input INPUT
                        input floor plan file (default: in/twoexitbottleneck.py)
                        
  -n NUMPEOPLE, --numpeople NUMPEOPLE
                        number of people in the simulation (default: 10)
                        
  -r RANDOM_STATE, --random_state RANDOM_STATE
                        aka. seed (default: 8675309)
                        
  -t MAX_TIME, --max_time MAX_TIME
                        the building collapses at this clock tick. people
                        beginning movement before this will be assumed to have
                        moved away sufficiently (no default argument)
                        
  -d FIRE_RATE, --fire_rate FIRE_RATE
                        exponent of spread of fire rate function exponentiator
                        fire grows exponentially. d determines how exponentially.
                        
  -b BOTTLENECK_DELAY, --bottleneck_delay BOTTLENECK_DELAY
                        how long until the next person may leave the B
                        
  -a ANIMATION_DELAY, --animation_delay ANIMATION_DELAY
                        delay per frame of animated visualization (s, default: 1)
                        
  -f, --no_spread_fire  disallow fire to spread around? (default: false)
  
  -g, --no_graphical_output
                        disallow graphics? (default: false)
                        
  -v, --verbose         show excessive output? (default: false)
                         
```

### Sample output
The goal of the program is to run simulations and output useful statistics
about the simulations, in a manner that helps understand the effects of
various parameters the simulation is called with, on the outcome.
```
STATS
	 total # people .......................................... 32
	 # people safe ........................................... 32
	 # people dead ............................................ 0
	 # people gravely injured ................................. 0

	 average time to safe ................................ 10.088
```


Model
---
We model a floor plan as a 2D grid. A cell neighbors four other cells (top, bottom, left, right).
Each cell has attributes: it can be normal (N), wall (W), bottleneck (B), fire (F), safe zone (S), or people (P).
You can use a GUI program to design and generate input per our specification; 
visit [this repository](https://github.com/aalok-sathe/egress-floorplan-design). Some sample inputs are available in `in/`.

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



People
---
- Aalok S
- Nick B
- Matthew J

