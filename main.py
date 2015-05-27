# -*- coding: utf-8 -*-
import io, sys
from printer import *
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if __name__ == '__main__':
    old = OldPrinter('こんばんはよろしくお願いいたします')
    old.print()
    new = NewPrinter('こんばんはよろしくお願いいたします')
    new.print()