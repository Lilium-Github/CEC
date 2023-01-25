#pragma once
#include"gameobject.h"
//these functions help us dynamically create duck and star objects 
class factory {
public:
    virtual gameObject* create() = 0;
};
class StarFactory :public factory {
public:
    star* create() { return new star(); }
};
class DuckFactory :public factory {
public:
    duck* create() { return new duck(); }
};
class InvaderFactory :public factory {
public:
    invader* create() { return new invader(); }
};