"""
Functions Of Sets :
👉 .add  =>for adding something.it will add randomly because it does
           not have any order.
👉 .pop  => this will remove anything randomly from the set
👉 .remove => if we have to remove some value specific
              then we can use this .remove("anyvalue") instead of .pop()
👉 .discard  => it work same just like .remove()
                it can also be use if we want to remove some value specifically.
👉 .copy    => copy whole set.

👉 .isDisjoint() => the disjoint will check 2 or more than 2 sets that
                    for example if i want to check set b isdisjoint of set a
                    so this will return true or false.
                    disjoint mean that is all the element of the other
                    set are present or not. example given below
                    disjoint ka matlab hai k aik b element aik set ka wo dosray mein mojood hai k nai
                    agar agar aik b element mojood na ho tu ye dono sets disjoint hongay
                    orr ye true return karega. disjoint mean aik dono k bilkul opposite.
👉 .isSubset() =>   agar aik set k saray k saray element dosray set mein present hongay tu
                    tu wo wala set dosray ka subset hoga. subset name say hi zahir hai.

👉 .isSuperSet() => superset name say hi zahir hai k agar hm check krna chahein k like
                    c is superset of a tu iss ka mean hai k hm check krna chah rahay hain k
                    a k saray element jo hain wo c mein present hai ya nai.. k matlab
                    kay c iss iss ka super set hai. tu agar saray element present hongay tu
                    true return hoga wrna false.
👉.update() =>      this will simply return us the UNION of two sets
                    if we want the union of two sets we can use .update()
                    it will remove the duplicate values while add all other values.
👉.clear() =>       will clear all the set mean will delete all the elements from sets.
"""

a = {"ironman", "spider", "man", "hulk"}
a.add("thor")
print(a)
#
# a.pop()  # will remove anything randomly.
# print(a)


# a.add("random..")
# print(a)


# a.remove("spider")
# print(a)


bb = a.copy()
print(bb)


print("-"*100)

sett1 = {"ironamn", "hulk", "thiss", "captain"}
sett2 = {"superman", "hulk", "batman", "wonder-woman"}
# sett2 = {"ironamn", "hulk", "thiss", "captain"}
sett3 = {"hulk", "thor"}
sett4 = {"kah", "ali", "hulk", "captain", "spider", "ironamn", "thiss"}

print(sett1.isdisjoint(sett2))
print(sett1.issubset(sett2))
print(sett1.issubset(sett4))

print('-----')
print(sett4.issuperset(sett2))
sett1.update(sett4)

print(sett1)

a.clear()  # this will clear all the values from set a
