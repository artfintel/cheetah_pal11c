//
//  cheetah.h
//  cheetah
//
//  Created by Anton Barty on 11/04/12.
//  Copyright (c) 2012 CFEL. All rights reserved.
//

#ifndef CHEETAH_H
#define CHEETAH_H
#include "myTimer.h"
#include "peakfinders.h"
#include "detectorObject.h"
#include "cheetahGlobal.h"
#include "cheetahEvent.h"
#include "cheetahmodules.h"


int cheetahInit(cGlobal *);
void cheetahNewRun(cGlobal *);
cEventData* cheetahNewEvent(cGlobal	*global);
void cheetahProcessEvent(cGlobal *, cEventData *);
void cheetahProcessEventMultithreaded(cGlobal *, cEventData *);
void cheetahDestroyEvent(cEventData *);
void cheetahExit(cGlobal *);
void cheetahUpdateGlobal(cGlobal *, cEventData *);
#endif
