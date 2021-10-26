

for i in range(10):
    try: exec(open('script.py').read())
    except Exception as e: print(e)
    finally: print("Done")

