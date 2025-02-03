import datetime
import time

x = datetime.datetime.now()

y = time.time()


print(f"Seconds since January 1, 1970: {y:,.4f} or {y:.2e} in scientific notation")
print(x.strftime("%b"), x.strftime("%d"), x.strftime("%Y"), sep=" ")

print(x.strftime("%b %d %Y"))

print(f"{x.strftime('%b')} {x.strftime('%d')} {x.strftime('%Y')}")


