

print([n for n in range(1001) if n %7 == 0])
print([n for n in range(1001) if "3" in str(n)])
print("Lorem ipsum dolor sit amet, consectetur".count(" "))

s = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
print(sorted({c for c in list(s.lower()) if c not in "aeiou "}))
