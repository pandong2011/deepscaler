"""Dataset type definitions for DeepScaler.

This module defines enums for training and testing datasets used in DeepScaler,
as well as a union type for both dataset types.
"""

import enum
from typing import Union


class TrainDataset(enum.Enum):
    """Enum for training datasets.
    Contains identifiers for various math problem datasets used during training.


    AIME = ' 美国数学邀请赛 ' # American Invitational Mathematics Examination（美国数学邀请赛）
    AMC = ' 美国数学竞赛 ' # American Mathematics Competition（美国数学竞赛）
    OMNI_MATH = ' 全知数学 ' # Omni Math（全知数学，这里 “Omni” 直译为 “全知的、无所不包的”，意译了一下）
    NUMINA_OLYMPIAD = ' 奥林匹克竞赛 ' # Unique Olympiad problems from NUMINA（来自 NUMINA 的独特奥林匹克竞赛题目）
    MATH = ' 数学 ' # Dan Hendrycks Math Problems（丹・亨德里克斯数学题）
    STILL = 'STILL 数据集 ' # STILL dataset（STILL 数据集）
    DEEPSCALER = ' 深度缩放器 ' # （包含美国数学邀请赛、美国数学竞赛、全知数学、丹・亨德里克斯数学题、STILL 数据集））
    """
    AIME = 'AIME'  # American Invitational Mathematics Examination
    AMC = 'AMC'  # American Mathematics Competition
    OMNI_MATH = 'OMNI_MATH'  # Omni Math
    NUMINA_OLYMPIAD = 'OLYMPIAD'  # Unique Olympiad problems from NUMINA
    MATH = 'MATH'  # Dan Hendrycks Math Problems
    STILL = 'STILL'  # STILL dataset
    DEEPSCALER = 'DEEPSCALER'  # DeepScaler (AIME, AMC, OMNI_MATH, MATH, STILL)


class TestDataset(enum.Enum):
    """Enum for testing/evaluation datasets.
    
    Contains identifiers for datasets used to evaluate model performance.
    """
    AIME = 'AIME'  # American Invitational Mathematics Examination
    AMC = 'AMC'  # American Mathematics Competition
    MATH = 'MATH'  # Math 500 problems
    MINERVA = 'MINERVA'  # Minerva dataset
    OLYMPIAD_BENCH = 'OLYMPIAD_BENCH'  # Olympiad benchmark problems


"""Type alias for either training or testing dataset types."""
Dataset = Union[TrainDataset, TestDataset]
