"""
Classes from the 'PencilKit' framework.
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


PKLegacyDrawingRegressionTester = _Class("PKLegacyDrawingRegressionTester")
PKTextInputHandwritingController = _Class("PKTextInputHandwritingController")
PKTextInputDebugLogEntry = _Class("PKTextInputDebugLogEntry")
PKTextInputDebugArchivedLogEntry = _Class("PKTextInputDebugArchivedLogEntry")
PKTextInputDebugRecordingLogEntry = _Class("PKTextInputDebugRecordingLogEntry")
PKInputPointUtility = _Class("PKInputPointUtility")
PKReplicaManager = _Class("PKReplicaManager")
PKReplicaEntry = _Class("PKReplicaEntry")
PKImageCompare = _Class("PKImageCompare")
PKMetalLiveStrokePaintRenderCache = _Class("PKMetalLiveStrokePaintRenderCache")
PKMetalLiveStrokePaintRenderCacheBuffer = _Class(
    "PKMetalLiveStrokePaintRenderCacheBuffer"
)
PKVectorMultiTimestamp = _Class("PKVectorMultiTimestamp")
PKVectorTimestamp = _Class("PKVectorTimestamp")
PKVectorTimestampElement = _Class("PKVectorTimestampElement")
PKIntersectionResult = _Class("PKIntersectionResult")
PKTileController = _Class("PKTileController")
PKLiveStrokesParticlesAnimation = _Class("PKLiveStrokesParticlesAnimation")
PKStrokeGenerator = _Class("PKStrokeGenerator")
PKSelectionStatisticsManager = _Class("PKSelectionStatisticsManager")
PKSelectionStatisticsSession = _Class("PKSelectionStatisticsSession")
PKFakeTapToFocusDelegate = _Class("PKFakeTapToFocusDelegate")
_PKFakeTapToFocusInfo = _Class("_PKFakeTapToFocusInfo")
PKFakeDisableDelegate = _Class("PKFakeDisableDelegate")
_PKFakeFixInfo = _Class("_PKFakeFixInfo")
PKFakeCalendarLocationDelegate = _Class("PKFakeCalendarLocationDelegate")
PKFakeVoiceMemosDelegate = _Class("PKFakeVoiceMemosDelegate")
PKFakeNotesDelegate = _Class("PKFakeNotesDelegate")
PKTextInputFakeInteractions = _Class("PKTextInputFakeInteractions")
PKIndexableContent = _Class("PKIndexableContent")
PKFloatRange = _Class("PKFloatRange")
PKSpaceInsertionController = _Class("PKSpaceInsertionController")
UITextViewDrawingInfo = _Class("UITextViewDrawingInfo")
PKTextInputUITextInputInterface = _Class("PKTextInputUITextInputInterface")
PKShapeDrawingController = _Class("PKShapeDrawingController")
PKPaletteConcreteBaseTool = _Class("PKPaletteConcreteBaseTool")
PKPaletteConcreteHandwritingTool = _Class("PKPaletteConcreteHandwritingTool")
PKLassoRenderer = _Class("PKLassoRenderer")
PKSelectionViewShapeSupportCache = _Class("PKSelectionViewShapeSupportCache")
PKRendererTileProperties = _Class("PKRendererTileProperties")
PKRecognitionSessionManager = _Class("PKRecognitionSessionManager")
PKTitleQueryItem = _Class("PKTitleQueryItem")
PKPaletteInputAssistantButtonProvider = _Class("PKPaletteInputAssistantButtonProvider")
PKMetalResourceHandlerBuffer = _Class("PKMetalResourceHandlerBuffer")
PKPaletteTapToRadarConfiguration = _Class("PKPaletteTapToRadarConfiguration")
PKPaletteTapToRadarCommand = _Class("PKPaletteTapToRadarCommand")
PKMetalFramebuffer = _Class("PKMetalFramebuffer")
PKTextInputRecognitionManager = _Class("PKTextInputRecognitionManager")
PKTextInputResultCommand = _Class("PKTextInputResultCommand")
PKMetalResourceHandler = _Class("PKMetalResourceHandler")
PKSearchQueryItem = _Class("PKSearchQueryItem")
PKPaletteColorPickerControllerFactory = _Class("PKPaletteColorPickerControllerFactory")
PKPaletteBaseColorPickerController = _Class("PKPaletteBaseColorPickerController")
PKPaletteSystemColorPickerController = _Class("PKPaletteSystemColorPickerController")
PKPaletteStandardColorPickerController = _Class(
    "PKPaletteStandardColorPickerController"
)
PKMetalBuffer = _Class("PKMetalBuffer")
PKClusteringUtility = _Class("PKClusteringUtility")
PKVersionedDocument = _Class("PKVersionedDocument")
PKDrawingVersionedDocument = _Class("PKDrawingVersionedDocument")
PKMetalPaintRenderCache = _Class("PKMetalPaintRenderCache")
PKMetalPaintRenderCacheBuffer = _Class("PKMetalPaintRenderCacheBuffer")
PKPaletteController = _Class("PKPaletteController")
PKPaletteScaleFactorPolicy = _Class("PKPaletteScaleFactorPolicy")
PKTextInputTargetState = _Class("PKTextInputTargetState")
PKDataDetectorItem = _Class("PKDataDetectorItem")
PKCanvasSessionStatisticsManager = _Class("PKCanvasSessionStatisticsManager")
PKSettingsDaemon = _Class("PKSettingsDaemon")
PKDrawingPaletteStatisticsEventLogger = _Class("PKDrawingPaletteStatisticsEventLogger")
PKStatisticsManager = _Class("PKStatisticsManager")
PKStrokeSpatialCache = _Class("PKStrokeSpatialCache")
PKMetalRenderer = _Class("PKMetalRenderer")
PKPaletteTransition = _Class("PKPaletteTransition")
PKPaletteFloatingKeyboardController = _Class("PKPaletteFloatingKeyboardController")
PKAccessibility = _Class("PKAccessibility")
PKAlternativeStrokesAnimation = _Class("PKAlternativeStrokesAnimation")
PKInkModifier = _Class("PKInkModifier")
PKVisualizationManager = _Class("PKVisualizationManager")
PKInkToolMinimizedImageFactory = _Class("PKInkToolMinimizedImageFactory")
PKPathUtility = _Class("PKPathUtility")
PKTranscriptionController = _Class("PKTranscriptionController")
PKTranscriptionResult = _Class("PKTranscriptionResult")
PKStrokeProviderSliceIdentifier = _Class("PKStrokeProviderSliceIdentifier")
PKImageRenderer = _Class("PKImageRenderer")
PKTextInputWritingSession = _Class("PKTextInputWritingSession")
PKDrawingPowerSavingController = _Class("PKDrawingPowerSavingController")
PKFadeOutStrokeAnimation = _Class("PKFadeOutStrokeAnimation")
PKSwatchColor = _Class("PKSwatchColor")
PKPaletteKeyboardUtilities = _Class("PKPaletteKeyboardUtilities")
PKRulerController = _Class("PKRulerController")
PKMetalParticleRenderCache = _Class("PKMetalParticleRenderCache")
PKMetalParticleRenderCacheBuffer = _Class("PKMetalParticleRenderCacheBuffer")
PKSelectionController = _Class("PKSelectionController")
PKSelectionInteraction = _Class("PKSelectionInteraction")
PKSelectionInput = _Class("PKSelectionInput")
PKStrokeProvider = _Class("PKStrokeProvider")
PKTextInputStrokeProvider = _Class("PKTextInputStrokeProvider")
PKTextInputDebugLogEntryRerun = _Class("PKTextInputDebugLogEntryRerun")
PKSelectionHighlightRenderer = _Class("PKSelectionHighlightRenderer")
PKStroke = _Class("PKStroke")
_PKClippedStroke = _Class("_PKClippedStroke")
PKMutableStroke = _Class("PKMutableStroke")
PKStrokeSelectionImage = _Class("PKStrokeSelectionImage")
PKStrokeSelectionImageConfig = _Class("PKStrokeSelectionImageConfig")
PKStrokeSelection = _Class("PKStrokeSelection")
PKPaintAreaViewSurface = _Class("PKPaintAreaViewSurface")
PKTextInputElementContent = _Class("PKTextInputElementContent")
PKMetalShader = _Class("PKMetalShader")
PKUndoCommand = _Class("PKUndoCommand")
PKModifyStrokeInkCommand = _Class("PKModifyStrokeInkCommand")
PKModifyStrokesCommand = _Class("PKModifyStrokesCommand")
PKSliceStrokesCommand = _Class("PKSliceStrokesCommand")
PKTransformStrokesCommand = _Class("PKTransformStrokesCommand")
PKPencilTextInputElementInteractionWrapper = _Class(
    "PKPencilTextInputElementInteractionWrapper"
)
PKPencilTouchDetection = _Class("PKPencilTouchDetection")
PKTransformStrokesAnimation = _Class("PKTransformStrokesAnimation")
PKInkParticleDescriptor = _Class("PKInkParticleDescriptor")
PKInkFunction = _Class("PKInkFunction")
PKDrawing = _Class("PKDrawing")
PKInterpolateColorAnimation = _Class("PKInterpolateColorAnimation")
PKRecognitionSessionCache = _Class("PKRecognitionSessionCache")
PKMetalRendererController = _Class("PKMetalRendererController")
PKTextInputDebugSharpenerLog = _Class("PKTextInputDebugSharpenerLog")
PKMetalStrokeRenderCache = _Class("PKMetalStrokeRenderCache")
PKMetalStrokeRenderCacheBuffer = _Class("PKMetalStrokeRenderCacheBuffer")
PKScribbleInteractionWrapper = _Class("PKScribbleInteractionWrapper")
PKShape = _Class("PKShape")
PKTextInputHandwritingShot = _Class("PKTextInputHandwritingShot")
PKMetalRenderState = _Class("PKMetalRenderState")
PKRendererVSyncController = _Class("PKRendererVSyncController")
PKTool = _Class("PKTool")
PKHandwritingTool = _Class("PKHandwritingTool")
PKLassoTool = _Class("PKLassoTool")
PKEraserTool = _Class("PKEraserTool")
PKInkingTool = _Class("PKInkingTool")
PKDataDetectorQueryItem = _Class("PKDataDetectorQueryItem")
PKStrokePoint = _Class("PKStrokePoint")
PKHandwritingDebugUtility = _Class("PKHandwritingDebugUtility")
PKStrokeRenderMask = _Class("PKStrokeRenderMask")
PKStrokePath = _Class("PKStrokePath")
PKColorMatrixViewPoint = _Class("PKColorMatrixViewPoint")
PKStrokeDelta = _Class("PKStrokeDelta")
PKLRUCache = _Class("PKLRUCache")
PKLRUCacheItem = _Class("PKLRUCacheItem")
PKRecognitionQueryController = _Class("PKRecognitionQueryController")
PKDispatchAfterHandler = _Class("PKDispatchAfterHandler")
PKDispatchAfterBlocks = _Class("PKDispatchAfterBlocks")
PKPaletteShape = _Class("PKPaletteShape")
PKLinedPaper = _Class("PKLinedPaper")
PKTextInputElement = _Class("PKTextInputElement")
PKDrawingReplayController = _Class("PKDrawingReplayController")
PKDrawingReplayPoint = _Class("PKDrawingReplayPoint")
PKTitleQuery = _Class("PKTitleQuery")
PKTiledCanvasViewDisplayLinkDelegate = _Class("PKTiledCanvasViewDisplayLinkDelegate")
PKPencilTextInputElement = _Class("PKPencilTextInputElement")
PKPencilTextInputElementInteraction = _Class("PKPencilTextInputElementInteraction")
PKStrokeProviderSlice = _Class("PKStrokeProviderSlice")
PKTextInputLanguageSpec = _Class("PKTextInputLanguageSpec")
PKRendererTileController = _Class("PKRendererTileController")
PKSelectionGlowRenderer = _Class("PKSelectionGlowRenderer")
PKSelectionTileProperties = _Class("PKSelectionTileProperties")
PKController = _Class("PKController")
PKQuery = _Class("PKQuery")
PKTranscriptionQuery = _Class("PKTranscriptionQuery")
PKDataDetectorQuery = _Class("PKDataDetectorQuery")
PKGroupQuery = _Class("PKGroupQuery")
PKStrokeGroupItem = _Class("PKStrokeGroupItem")
_PKStrokeClipPlane = _Class("_PKStrokeClipPlane")
PKTextInputTextPlaceholder = _Class("PKTextInputTextPlaceholder")
PKTextAttachmentDrawingViewProvider = _Class("PKTextAttachmentDrawingViewProvider")
PKPaletteViewInteraction = _Class("PKPaletteViewInteraction")
PKToolPicker = _Class("PKToolPicker")
PKScribbleInteraction = _Class("PKScribbleInteraction")
PKInkProperties = _Class("PKInkProperties")
PKInkFeatheringDescriptor = _Class("PKInkFeatheringDescriptor")
PKInkSmoothingDescriptor = _Class("PKInkSmoothingDescriptor")
PKInkRenderingDescriptor = _Class("PKInkRenderingDescriptor")
PKInkBehavior = _Class("PKInkBehavior")
PKInkParser = _Class("PKInkParser")
PKInkKey = _Class("PKInkKey")
PKInkManager = _Class("PKInkManager")
PKInk = _Class("PKInk")
PencilKit_Localization = _Class("PencilKit_Localization")
PKMetalUtility = _Class("PKMetalUtility")
PKTextInputFeedbackRect = _Class("PKTextInputFeedbackRect")
PKTextInputTextSelectionRect = _Class("PKTextInputTextSelectionRect")
PKHandwritingFeedbackActivity = _Class("PKHandwritingFeedbackActivity")
PKTextInputWindowFirstResponder = _Class("PKTextInputWindowFirstResponder")
PKTextInputUtilities = _Class("PKTextInputUtilities")
PKTextInputElementsFinder = _Class("PKTextInputElementsFinder")
PKTextInputSingleElementFinder = _Class("PKTextInputSingleElementFinder")
PKTextInputDebugStateIntrospector = _Class("PKTextInputDebugStateIntrospector")
PKTextInputElementsController = _Class("PKTextInputElementsController")
PKPencilTouchDetectionService = _Class("PKPencilTouchDetectionService")
PKTextInputAnalyticsController = _Class("PKTextInputAnalyticsController")
PKTextInputKeyboardSuppressionPolicyDelegate = _Class(
    "PKTextInputKeyboardSuppressionPolicyDelegate"
)
PKTextInputDebugLogController = _Class("PKTextInputDebugLogController")
PKTextInputReserveSpaceController = _Class("PKTextInputReserveSpaceController")
PKTextInputCursorController = _Class("PKTextInputCursorController")
PKTextInputWindowFirstResponderController = _Class(
    "PKTextInputWindowFirstResponderController"
)
PKTextInputPaletteController = _Class("PKTextInputPaletteController")
PKTextInputFeedbackController = _Class("PKTextInputFeedbackController")
PKTextInputCanvasController = _Class("PKTextInputCanvasController")
PKTextInputSettings = _Class("PKTextInputSettings")
PKTextInputInteraction = _Class("PKTextInputInteraction")
_PKTextInputInteraction = _Class("_PKTextInputInteraction")
PKTextInputKeyboardAssistantItem = _Class("PKTextInputKeyboardAssistantItem")
PKFakeUITapGestureForRequirements = _Class("PKFakeUITapGestureForRequirements")
_PKSpringLoadingGestureRecognizer = _Class("_PKSpringLoadingGestureRecognizer")
PKTextAttachmentDrawingViewTouchRecognizer = _Class(
    "PKTextAttachmentDrawingViewTouchRecognizer"
)
PKTextInputTouchDetectionGestureRecognizer = _Class(
    "PKTextInputTouchDetectionGestureRecognizer"
)
PKPencilTouchDetectionGestureRecognizer = _Class(
    "PKPencilTouchDetectionGestureRecognizer"
)
PKFreeTransformGestureRecognizer = _Class("PKFreeTransformGestureRecognizer")
PKRulerGestureRecognizer = _Class("PKRulerGestureRecognizer")
PKDrawingGestureRecognizer = _Class("PKDrawingGestureRecognizer")
PKTextInputDrawingGestureRecognizer = _Class("PKTextInputDrawingGestureRecognizer")
PKRendererTile = _Class("PKRendererTile")
PKRulerLayer = _Class("PKRulerLayer")
PKSelectionModificationKnob = _Class("PKSelectionModificationKnob")
PKSelectionTile = _Class("PKSelectionTile")
PKDataDetectorView = _Class("PKDataDetectorView")
PKColorPickerCrosshairView = _Class("PKColorPickerCrosshairView")
PKPaletteToolPickerView = _Class("PKPaletteToolPickerView")
PKPaletteToolPickerOverlayView = _Class("PKPaletteToolPickerOverlayView")
PKTextInputFloatingBackgroundView = _Class("PKTextInputFloatingBackgroundView")
_PKSliderKnobView = _Class("_PKSliderKnobView")
_PKHueSpectrumView = _Class("_PKHueSpectrumView")
_PKInkAttributesPickerView = _Class("_PKInkAttributesPickerView")
PKInlineInkPickerItem = _Class("PKInlineInkPickerItem")
PKTextInputGestureFeedbackView = _Class("PKTextInputGestureFeedbackView")
PKPaletteAdditionalOptionsView = _Class("PKPaletteAdditionalOptionsView")
PKSelectionGestureView = _Class("PKSelectionGestureView")
PKSpaceInsertionView = _Class("PKSpaceInsertionView")
_PKInkAttributesOpacityLabel = _Class("_PKInkAttributesOpacityLabel")
PKPaletteToolPickerArrowIndicatorView = _Class("PKPaletteToolPickerArrowIndicatorView")
PKDrawingPaletteInputAssistantContainerView = _Class(
    "PKDrawingPaletteInputAssistantContainerView"
)
PKPaletteToolPickerContainerView = _Class("PKPaletteToolPickerContainerView")
_PKColorPickerSimpleCrosshairView = _Class("_PKColorPickerSimpleCrosshairView")
PKPaletteContainerView = _Class("PKPaletteContainerView")
_PKToolIndicator = _Class("_PKToolIndicator")
PKPaletteToolPreview = _Class("PKPaletteToolPreview")
PKInlineColorPicker = _Class("PKInlineColorPicker")
PKPalettePencilInteractionFeedbackHostView = _Class(
    "PKPalettePencilInteractionFeedbackHostView"
)
PKTextAttachmentDrawingResizeView = _Class("PKTextAttachmentDrawingResizeView")
PKPaletteColorPickerView = _Class("PKPaletteColorPickerView")
PKMetalView = _Class("PKMetalView")
PKDrawingPaletteInputAssistantView = _Class("PKDrawingPaletteInputAssistantView")
PKPaletteToolShadowPathView = _Class("PKPaletteToolShadowPathView")
_PKRulerShadowPathView = _Class("_PKRulerShadowPathView")
_PKLassoShadowPathView = _Class("_PKLassoShadowPathView")
_PKEraserShadowPathView = _Class("_PKEraserShadowPathView")
_PKMarkerShadowPathView = _Class("_PKMarkerShadowPathView")
_PKPenShadowPathView = _Class("_PKPenShadowPathView")
_PKPaletteHandwritingToolShadowPathView = _Class(
    "_PKPaletteHandwritingToolShadowPathView"
)
_PKPencilShadowPathView = _Class("_PKPencilShadowPathView")
PKPaletteUndoRedoView = _Class("PKPaletteUndoRedoView")
PKDragIndicatorView = _Class("PKDragIndicatorView")
PKPaletteHostView = _Class("PKPaletteHostView")
PKTexInputDebugContainerView = _Class("PKTexInputDebugContainerView")
PKPalettePencilInteractionFeedbackView = _Class(
    "PKPalettePencilInteractionFeedbackView"
)
PKDrawingAdjustmentKnob = _Class("PKDrawingAdjustmentKnob")
PKPaletteColorSwatch = _Class("PKPaletteColorSwatch")
PKPaletteMulticolorSwatch = _Class("PKPaletteMulticolorSwatch")
PKProgressAlertContentView = _Class("PKProgressAlertContentView")
_PKPathView = _Class("_PKPathView")
_PKAnimatableBorderCornerRadiusView = _Class("_PKAnimatableBorderCornerRadiusView")
PKRulerView = _Class("PKRulerView")
PKTextInputDebugReplayView = _Class("PKTextInputDebugReplayView")
PKPaletteTextOptionsView = _Class("PKPaletteTextOptionsView")
PKPaletteOptionCell = _Class("PKPaletteOptionCell")
PKPaletteOptionButtonCell = _Class("PKPaletteOptionButtonCell")
PKPaletteOptionLabelCell = _Class("PKPaletteOptionLabelCell")
PKPaletteOptionSwitchCell = _Class("PKPaletteOptionSwitchCell")
PKPaletteOptionCellDividerView = _Class("PKPaletteOptionCellDividerView")
PKRecognitionOverlayView = _Class("PKRecognitionOverlayView")
_PKColorPickerCrosshairCornerMaskView = _Class("_PKColorPickerCrosshairCornerMaskView")
PKPaintAreaView = _Class("PKPaintAreaView")
_PKInkToolOpacityLabel = _Class("_PKInkToolOpacityLabel")
_PKColorPickerView = _Class("_PKColorPickerView")
PKPaletteReturnKeyButtonContentView = _Class("PKPaletteReturnKeyButtonContentView")
PKPaletteToolPickerAndColorPickerView = _Class("PKPaletteToolPickerAndColorPickerView")
PKTextInputDebugTargetsView = _Class("PKTextInputDebugTargetsView")
PKPaletteColorPickerContainerView = _Class("PKPaletteColorPickerContainerView")
PKColorMatrixView = _Class("PKColorMatrixView")
PKPaletteView = _Class("PKPaletteView")
PKDrawingPaletteView = _Class("PKDrawingPaletteView")
PKUCBPaletteView = _Class("PKUCBPaletteView")
PKPaletteContentView = _Class("PKPaletteContentView")
PKPaletteButtonGroupView = _Class("PKPaletteButtonGroupView")
_PKCheckerGridView = _Class("_PKCheckerGridView")
PKPaletteShapesView = _Class("PKPaletteShapesView")
PKPaletteErasingAttributesView = _Class("PKPaletteErasingAttributesView")
PKAttachmentView = _Class("PKAttachmentView")
PKCanvasAttachmentView = _Class("PKCanvasAttachmentView")
_UITextAttachmentDrawingView = _Class("_UITextAttachmentDrawingView")
PKTextAttachmentDrawingView = _Class("PKTextAttachmentDrawingView")
_PKAllowDrawingWhilePresentingPopoverView = _Class(
    "_PKAllowDrawingWhilePresentingPopoverView"
)
PKTiledView = _Class("PKTiledView")
PKTiledTextView = _Class("PKTiledTextView")
PKAccessoryView = _Class("PKAccessoryView")
PKAdornmentView = _Class("PKAdornmentView")
PKSelectionView = _Class("PKSelectionView")
PKTiledCanvasView = _Class("PKTiledCanvasView")
PKTContainerView = _Class("PKTContainerView")
PKCanvasView = _Class("PKCanvasView")
_PKInlineDrawingScrollView = _Class("_PKInlineDrawingScrollView")
PKTextInputDebugViewTableCell = _Class("PKTextInputDebugViewTableCell")
PKTextInputDebugDrawingEntryCell = _Class("PKTextInputDebugDrawingEntryCell")
PKTextInputDebugLogTextCell = _Class("PKTextInputDebugLogTextCell")
PKPaletteShapeCell = _Class("PKPaletteShapeCell")
_PKColorAlphaSlider = _Class("_PKColorAlphaSlider")
PKInlineInkPicker = _Class("PKInlineInkPicker")
_PKInkThicknessButton = _Class("_PKInkThicknessButton")
PKPaletteToolView = _Class("PKPaletteToolView")
PKPaletteHandwritingToolView = _Class("PKPaletteHandwritingToolView")
PKPaletteSelectingToolView = _Class("PKPaletteSelectingToolView")
PKPaletteErasingToolView = _Class("PKPaletteErasingToolView")
PKPaletteInkingToolView = _Class("PKPaletteInkingToolView")
PKPaletteButton = _Class("PKPaletteButton")
PKPaletteKeyboardButton = _Class("PKPaletteKeyboardButton")
PKPaletteBarButtonItemButton = _Class("PKPaletteBarButtonItemButton")
PKPaletteReturnKeyButton = _Class("PKPaletteReturnKeyButton")
_PKInkThicknessPicker = _Class("_PKInkThicknessPicker")
_PKFlatInkToolButton = _Class("_PKFlatInkToolButton")
_PKEmbossedInkToolButton = _Class("_PKEmbossedInkToolButton")
_PKInkColorButton = _Class("_PKInkColorButton")
_PKEmbossedInkColorButton = _Class("_PKEmbossedInkColorButton")
_PKFlatInkColorButton = _Class("_PKFlatInkColorButton")
PKInkColorButton = _Class("PKInkColorButton")
_PKFlatColorPickerButton = _Class("_PKFlatColorPickerButton")
_PKEmbossedColorPickerButton = _Class("_PKEmbossedColorPickerButton")
PKTextInputDebugRadarViewController = _Class("PKTextInputDebugRadarViewController")
PKProgressContentViewController = _Class("PKProgressContentViewController")
PKRecognitionDataCollectionViewController = _Class(
    "PKRecognitionDataCollectionViewController"
)
PKTextInputDebugViewController = _Class("PKTextInputDebugViewController")
PKPaletteInputAssistantViewController = _Class("PKPaletteInputAssistantViewController")
PKPaletteTextOptionsViewController = _Class("PKPaletteTextOptionsViewController")
PKPaletteMoreOptionsViewController = _Class("PKPaletteMoreOptionsViewController")
PKColorPicker = _Class("PKColorPicker")
PKRecognitionDrawingPreviewViewController = _Class(
    "PKRecognitionDrawingPreviewViewController"
)
_PKDebugToolViewController = _Class("_PKDebugToolViewController")
PKPaletteShapesViewController = _Class("PKPaletteShapesViewController")
PKPaletteAttributeViewController = _Class("PKPaletteAttributeViewController")
PKInkAttributesPicker = _Class("PKInkAttributesPicker")
PKPaletteErasingAttributesViewController = _Class(
    "PKPaletteErasingAttributesViewController"
)
PKTextInputDebugSharpenerLogViewController = _Class(
    "PKTextInputDebugSharpenerLogViewController"
)
PKProgressAlertController = _Class("PKProgressAlertController")