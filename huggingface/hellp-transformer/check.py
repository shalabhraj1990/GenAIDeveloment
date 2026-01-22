import torch
print("Torch",torch.__version__)
print("xpu aviable:",torch.xpu.is_available())
print('Device count',torch.xpu.device_count())
if torch.xpu.is_available():
    print("Device name:",torch.xpu.get_device_name(0))
    