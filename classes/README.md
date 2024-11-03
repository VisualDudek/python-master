# CLASSES

Starting point: three kind of methods in class
TAKEAWAY: keep in mind signature of each function <- key for undertanding

**staticmethod** for me it is just to enable to call func from instance AND class + meta that func is related to class. Without staticmethod decorator you cannot create method that accept only arg without self-instance.

Rule of thumb: do not use staticmethods, use freestanding func. Except "can_multiply" or "is_somethig" ?

**classmethod** can be implemented as staticmethod BUT will break inheritance.
Can be:
- Alternative Constructor
- Managing Class-Level Data
- Implement Factory Method <- diff from alternative constructor