import shutil
import os 
import sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.constant import *
from flask import request
import pickle
from src.utils.main_utils import MainUtils