"""
Classes from the 'SampleAnalysis' framework.
"""

try:
    from rubicon.objc import ObjCClass
except ValueError:

    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None


SAWSUpdateDataStore = _Class("SAWSUpdateDataStore")
SAWSUpdateTimeToIndexMapping = _Class("SAWSUpdateTimeToIndexMapping")
SAWSUpdate = _Class("SAWSUpdate")
SAHIDEvent = _Class("SAHIDEvent")
SAHIDStep = _Class("SAHIDStep")
SAFanSpeed = _Class("SAFanSpeed")
SABinaryLocator = _Class("SABinaryLocator")
SATaskState = _Class("SATaskState")
SATaskStateKPerf = _Class("SATaskStateKPerf")
SATask = _Class("SATask")
PASampleTimeSeriesDataStore = _Class("PASampleTimeSeriesDataStore")
SAMountStatusTracker = _Class("SAMountStatusTracker")
SAMountStatus = _Class("SAMountStatus")
SAMountSnapshot = _Class("SAMountSnapshot")
SASamplePrintOptions = _Class("SASamplePrintOptions")
SASamplePrinter = _Class("SASamplePrinter")
SAStack = _Class("SAStack")
SAMicrostackshotSummary = _Class("SAMicrostackshotSummary")
SATimeRange = _Class("SATimeRange")
SATimestamp = _Class("SATimestamp")
SATaskThreadCallTrees = _Class("SATaskThreadCallTrees")
SACallTree = _Class("SACallTree")
SAThreadCallTree = _Class("SAThreadCallTree")
SATaskCallTree = _Class("SATaskCallTree")
SAExecutableCallTree = _Class("SAExecutableCallTree")
SACallTreeNode = _Class("SACallTreeNode")
SACallTreeState = _Class("SACallTreeState")
SACallTreeFrame = _Class("SACallTreeFrame")
SAObjectListEntry = _Class("SAObjectListEntry")
SADispatchQueueState = _Class("SADispatchQueueState")
SADispatchQueue = _Class("SADispatchQueue")
SATurnstileInfo = _Class("SATurnstileInfo")
SAWaitInfo = _Class("SAWaitInfo")
SAThreadState = _Class("SAThreadState")
SAThreadStateMicrostackshot = _Class("SAThreadStateMicrostackshot")
SAThreadStateKPerf = _Class("SAThreadStateKPerf")
SAThread = _Class("SAThread")
SAPAStyleSourceInfo = _Class("SAPAStyleSourceInfo")
SAPAStyleSymbol = _Class("SAPAStyleSymbol")
SAPAStyleSymbolOwner = _Class("SAPAStyleSymbolOwner")
SAPAStyleSymbolDataStore = _Class("SAPAStyleSymbolDataStore")
SAPAStyleMountSnapshot = _Class("SAPAStyleMountSnapshot")
SAPAStyleMountStatus = _Class("SAPAStyleMountStatus")
SAPAStyleMountStatusTracker = _Class("SAPAStyleMountStatusTracker")
SAPAStyleHIDEvent = _Class("SAPAStyleHIDEvent")
SAPAStyleFanSpeed = _Class("SAPAStyleFanSpeed")
SAPAStyleImageInfo = _Class("SAPAStyleImageInfo")
SAPAStyleTimeInsensitiveTaskData = _Class("SAPAStyleTimeInsensitiveTaskData")
SAPAStyleTaskData = _Class("SAPAStyleTaskData")
SAPAStyleTaskPrivateData = _Class("SAPAStyleTaskPrivateData")
SAPAStyleSample = _Class("SAPAStyleSample")
SAPAStyleFrame = _Class("SAPAStyleFrame")
SAPAStyleWaitInfo = _Class("SAPAStyleWaitInfo")
SAPAStyleThreadData = _Class("SAPAStyleThreadData")
SASourceInfo = _Class("SASourceInfo")
SASymbol = _Class("SASymbol")
SAInstruction = _Class("SAInstruction")
SASharedCache = _Class("SASharedCache")
SAKernelCache = _Class("SAKernelCache")
SABinaryLoadInfo = _Class("SABinaryLoadInfo")
SABinaryLoadInfoTrackingHighestOffset = _Class("SABinaryLoadInfoTrackingHighestOffset")
SABinaryLoadInfoZerothSegmentOnly = _Class("SABinaryLoadInfoZerothSegmentOnly")
SAUserBinaryLoadInfo = _Class("SAUserBinaryLoadInfo")
SAKernelBinaryLoadInfo = _Class("SAKernelBinaryLoadInfo")
SABinary = _Class("SABinary")
SASegment = _Class("SASegment")
SACSSymbolOwnerWrapper = _Class("SACSSymbolOwnerWrapper")
SAKPerfState = _Class("SAKPerfState")
SASampleStore = _Class("SASampleStore")
SABinaryToSymbolicate = _Class("SABinaryToSymbolicate")
SAAuxiliaryData = _Class("SAAuxiliaryData")
SAStackIterator = _Class("SAStackIterator")
SAFrameIterator = _Class("SAFrameIterator")
SAFrame = _Class("SAFrame")
SAUserTruncatedBacktrace = _Class("SAUserTruncatedBacktrace")
SAKernelFrame = _Class("SAKernelFrame")
SALeafFrame = _Class("SALeafFrame")
SAKernelLeafFrame = _Class("SAKernelLeafFrame")
SAException = _Class("SAException")
SAOutputStream = _Class("SAOutputStream")
SAMutableDataOutputStream = _Class("SAMutableDataOutputStream")
SAFileOutputStream = _Class("SAFileOutputStream")