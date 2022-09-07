
import time

# classe utilizzata per la misura del tempo di esecuzione dei singoli blocchi, da utilizzare
# in seguito con i with() statement per dare in output variabili contenenti il valore del
# tempo impiegato

class timer:
  def __init__(self, enter_fn=None, exit_fn=None):
    self.enter_fn = enter_fn
    self.exit_fn = exit_fn
  
  def __enter__(self):
    self.begin = time.perf_counter()
    self.end = self.begin
    if self.enter_fn:
      self.enter_fn(self.begin)
    return lambda: self.end - self.begin
  
  def __exit__(self, exc_type, exc_data, exc_tb):
    self.end = time.perf_counter()
    if self.exit_fn:
      self.exit_fn(self.begin, self.end)
