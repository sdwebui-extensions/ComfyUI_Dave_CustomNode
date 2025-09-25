# Made by Davemane42#0042 for ComfyUI
import os
import subprocess
import importlib.util
import sys
import filecmp
import shutil

WEB_DIRECTORY = "./javascript"



from .MultiAreaConditioning import MultiAreaConditioning, ConditioningUpscale, ConditioningStretch, ConditioningDebug
from .MultiLatentComposite import MultiLatentComposite
#from .ABGRemover import ABGRemover

NODE_CLASS_MAPPINGS = {
    "MultiLatentComposite": MultiLatentComposite,
    "MultiAreaConditioning": MultiAreaConditioning,
    "ConditioningUpscale": ConditioningUpscale,
    "ConditioningStretch": ConditioningStretch,
    #"ABGRemover": ABGRemover,
}

print('\033[34mDavemane42 Custom Nodes: \033[92mLoaded\033[0m')