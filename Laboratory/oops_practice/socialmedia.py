class Person:
    def __init__(self, name, age, bio, interests):
        self.name = name
        self.age = age
        self.bio = bio
        self.interests = interests
    def __str__(self):
        return f' {self.name} age: {self.age} bio: {self.bio} interests: {self.interests}'

    def UpdateBio(self, bio):
        self.bio = bio

    def AddInterests(self, i):
        self.interests.append(i)


class Network:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        self.people[person] = []

    def add_connection(self, person1, person2):
        if person1 in self.people:
            self.people[person1].append(person2)

        else:
            self.people[person1] = [person2]
        if person2 in self.people:
            self.people[person2].append(person1)
        else:
            self.people[person2] = [person1]

    def RemoveConnection(self, person1, person2):
        if person2 in self.people.person1:
            self.people[person1].remove(person2)
        if person2 in self.people.person1:
            self.people[person2].remove(person1)

    def CommonConnection(self, person1, person2):
        commonfriends = []
        if person1 in self.people:
            for friend in self.people[person1]:
                if friend in self.people[person2]:
                    commonfriends.append(friend)
        return commonfriends


graph = Network()

user1 = Person("johan", 28, "I am a programmer", ["football", "coding"])
user2 = Person("joe", 25, "I am a doctor", ["chess", "singing", "football"])
user3 = Person("jane", 23, "I am a lawyer", ["dancing", "singing", "football"])
user4 = Person("jim", 21, "I am a student", ["painting", "basketball"])

graph.add_person(user1)
graph.add_person(user2)
graph.add_person(user3)
graph.add_person(user4)

graph.add_connection(user1, user3)
graph.add_connection(user1, user4)
graph.add_connection(user2, user3)
graph.add_connection(user4, user2)

user1.UpdateBio("I am a programmer and I love to code")
user2.AddInterests("skiing")
query = graph.CommonConnection(user1, user2)

print(user1)
print(graph.CommonConnection(user1,user4))