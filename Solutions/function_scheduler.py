import time


def job_scheduler(f, n):
  time.sleep(n / 1000)
  f()


def my_function():
  print("Hello, World!")


if __name__ == "__main__":
  job_scheduler(my_function, 5000)
