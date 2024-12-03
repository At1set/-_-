class Clock:
  def __init__(self, TimeOfDay) -> None:
    self.TimeOfDay = TimeOfDay

  def getSeconds(self):
    return self.TimeOfDay - self.getHours() * 3600 - self.getMinutes() * 60
  def getMinutes(self):
    return (self.TimeOfDay - self.getHours() * 3600) // 60
  def getHours(self):
    return self.TimeOfDay // 3600
  
  def setSeconds(self, value):
    if value < 0 or value > 60: raise ValueError()
    oldTimeDay = Clock(self.TimeOfDay)

    self.TimeOfDay -= self.getSeconds()
    self.TimeOfDay += value

    if (self.getMinutes() != oldTimeDay.getMinutes() or
        self.getHours() != oldTimeDay.getHours()):
      self.TimeOfDay = oldTimeDay.TimeOfDay
      raise ValueError()

    return self.Invariant()
  
  def setMinutes(self, value):
    if value < 0 or value > 60: raise ValueError()
    oldTimeDay = Clock(self.TimeOfDay)

    self.TimeOfDay -= self.getMinutes() * 60
    self.TimeOfDay += value * 60

    if (self.getSeconds() != oldTimeDay.getSeconds() or
        self.getHours() != oldTimeDay.getHours()):
      self.TimeOfDay = oldTimeDay.TimeOfDay
      raise ValueError()

    return self.Invariant()
  
  def setHours(self, value):
    if value < 0 or value > 23: raise ValueError()
    oldTimeDay = Clock(self.TimeOfDay)

    self.TimeOfDay -= self.getHours() * 3600
    self.TimeOfDay += value * 3600

    if (self.getSeconds() != oldTimeDay.getSeconds() or
        self.getMinutes() != oldTimeDay.getMinutes()):
      self.TimeOfDay = oldTimeDay.TimeOfDay
      raise ValueError()

    return self.Invariant()
  
  def Invariant(self):
    if (self.TimeOfDay < 0 or self.TimeOfDay > 86400): raise ValueError()


def printTime(Clock: Clock):
  print(f"\r{Clock.getHours()}:{Clock.getMinutes()}:{Clock.getSeconds()}", end="")


def main():
  clock = Clock(86399)
  printTime(clock)

if __name__ == "__main__":
  main()