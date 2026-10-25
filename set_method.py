# we can manupulate the set using the methods provided by the set class in python. Here are some of the commonly used methods:

# Tuple = Locker 🔐
# You store things safely
# No one can change it
# Set = Bag 🎒
# You can add/remove items
# No duplicates allowed

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}

total_audience = insta_followers | youtube_followers

print(total_audience)

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}

total_audience = insta_followers.union(youtube_followers)

print(total_audience)


# there are two method to combine two sets in python. The first method is using the | operator and the second method is using the union() method. Both methods will give you the same result which is a new set that contains all the unique elements from both sets.

# if we have to update same set with the combined elements of two sets we can use the update() 

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
insta_followers.update(youtube_followers)
print(insta_followers, youtube_followers)

# intersection is basically if there is common element in both set then it will return that element otherwise it will return empty set.

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
kunal_followers=insta_followers.intersection(youtube_followers)
print(kunal_followers)


# if we have to only update the first set with the common elements of both sets we can use the intersection_update() method.

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
insta_followers.intersection_update(youtube_followers)
print(insta_followers)

# symetrric_difference print the non common element in both set. It will return a new set that contains all the elements that are in either of the sets but not in both.


insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
kunal_followers=insta_followers.symmetric_difference(youtube_followers)
print(kunal_followers)


# in diffrent set method we can use the difference() method to get the non common element in both set. It will return a new set that contains all the elements that are in
#  the first set but not in the second set.

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
kunal_followers=insta_followers.difference(youtube_followers)
print(kunal_followers)

# isdisjoint is used to show the both the sets have same value or if its yes that show true and its no that show false

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
print(insta_followers.isdisjoint(youtube_followers))


insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
print(insta_followers.issuperset(youtube_followers))


insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
print(insta_followers.issubset(youtube_followers))


# if we have to add item in set we use .add before the set name example


insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
insta_followers.add("badwa")
print(insta_followers)

# if we have to remove value we use .remove

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
insta_followers.remove("kunal")
print(insta_followers)

# distart works like remove but the diffrence is that its cannot shows errors

insta_followers = {"rahul", "aman", "kunal"}
youtube_followers = {"kunal", "rohit"}
insta_followers.discard("kunal2")
print(insta_followers)

# pop is use to show the one value in the sets 

insta_followers = {"rahul", "aman", "kunal"}
item = insta_followers.pop()
print(item)

# del method is use to delele the entire set

insta_followers = {"rahul", "aman", "kunal"}
item = insta_followers.pop()
del insta_followers
print(item)

# us the if function in the set

insta_followers = {"rahul", "aman", "kunal"}
if "kunal" in  insta_followers:
    print("karla is present")
else:
    print("badwa")






