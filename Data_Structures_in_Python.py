📦 Tuples
A tuple is an ordered, immutable collection.
Once created, you cannot modify (add, remove, or change) its elements.

🔹 When to Use:
✅ Storing fixed data (e.g., coordinates, config values)
✅ Faster performance compared to lists
✅ Can be used as dictionary keys (because they're immutable)
✅ When you want to return multiple values from a function
example = (10, 20)
# example[0] = 30  ❌ This will raise an error


📋 Lists
A list is an ordered, mutable collection.
You can modify its contents (append, remove, or change items).

🔹 When to Use:
✅ When storing a dynamic sequence of items
✅ You need to add, remove, or change elements frequently
✅ You need to sort or reverse items

fruits = ["🍎", "🍌", "🍒"]
fruits.append("🥭")  # Add an item
fruits[1] = "🍊"     # Change an item
print(fruits)        # ['🍎', '🍊', '🍒', '🥭']


🔢 Ranges
A range generates a sequence of numbers without storing them in memory like a list.
It's great for iteration and performance.

🔹 When to Use:
✅ You need a sequence of numbers (e.g., in loops)
✅ You care about memory efficiency and speed

for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4

print(list(range(2, 10, 2)))  # [2, 4, 6, 8]


♻️ Mutability
Mutability refers to whether an object can be changed after creation.

✅ Mutable: Can be modified
Examples: list, dict, set

❌ Immutable: Cannot be changed
Examples: tuple, str, int

# Mutable Example
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] — a changed too!

# Immutable Example
x = (1, 2)
y = x + (3,)
print(x)  # (1, 2)
print(y)  # (1, 2, 3)








