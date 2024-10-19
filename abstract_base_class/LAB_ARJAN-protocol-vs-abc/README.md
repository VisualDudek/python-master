Main README for this LAB, now futher readmes deeper 

Top overview
1. U can have service to which devices can be attached via `register_device()` method.
2. U cand create small program in form of list of messages
3. that programs can be run on given service via `run_program(List[Message])` method
4. apart from service methods you can collect diagnositcs on any device
5. nice separation of functionality in separate files: device, devices, service, message, diagnostics

# abc
- Device subclass of ABC defined in separate file.
- devices.py implements several subclasses of Device
- **Takeaway** we are using AND importing Device class everywhere, BUT does diagnostics really needs to know how to connect, disconnect and send_message ?
- huge advantage if ABC is that it will explicite state what need to be implementd AND IDE intergration via inheritance


# protocols
using protocols instead of ABCs
- **Takeaway** protocols defines the interface taht is expected (**holy grail of understainding**) -> in the part of the program that refers to it -> DEFAIN protocols in the parts of program when needed, NOT in separate file -> decoupling, reduce coupling
1. HUGE mind setup shift: define interface using protocols as close as posible to code where it is needed. No single huge class definition.
2. U do not need `device.py` file, now you can define Interface with needed methods directly where is needed, -> will not need `from iot.device import Device` anymore
3. After refactor:
   1. Protocol that define Device interface now is moved to service (where is used)
   3. Add Protocol into diagnostic and rename interface to `DiagnosticSource` bc that interface use only `status_update()` method from original `Device` abstract class 