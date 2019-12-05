#evacuation.py
import simulus 
import sys
import person
import random


def updateBottleNecks(self, bottlenecks):
	#Add updating implementation
	sim.sched(updateBottleNecks, offset = 1)
	pass


#initialize list of Person()
numPeople = 100 #set this
people = []
positions = []
bottlenecks = []
for i in numPeople:
	people.append(person.Person(
		random.uniform(0.5, 4), 
		random.uniform(0.5, 1.0), 
		*random.sample(positions, 1))


#start simulation (simulus)
sim = simulus.simulation()

#update bottlenecks 
sim.sched(updateBottleNecks, offset = 1)

#schedule initial movements for each Person() using their rate 
for i in numPeople:
	sim.sched(people[i].move, graph, sim, offset = people[i].rate)

