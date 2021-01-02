"""
Classes from the 'PersonalizationPortrait' framework.
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


PPNamedEntityQuery = _Class("PPNamedEntityQuery")
PPConfigStore = _Class("PPConfigStore")
PPNotification = _Class("PPNotification")
PPContactQuery = _Class("PPContactQuery")
PPConnectionsStore = _Class("PPConnectionsStore")
PPPostalAddress = _Class("PPPostalAddress")
PPTopicRecord = _Class("PPTopicRecord")
PPMutableTopicRecord = _Class("PPMutableTopicRecord")
PPTopic = _Class("PPTopic")
PPTopicWithRecord = _Class("PPTopicWithRecord")
PPTripPart = _Class("PPTripPart")
PPScoredEvent = _Class("PPScoredEvent")
PPTripEvent = _Class("PPTripEvent")
PPHighlightedEvent = _Class("PPHighlightedEvent")
PPSuggestedEvent = _Class("PPSuggestedEvent")
PPFeedbackItem = _Class("PPFeedbackItem")
PPContact = _Class("PPContact")
PPContactNameRecord = _Class("PPContactNameRecord")
PPClientContactNameRecord = _Class("PPClientContactNameRecord")
PPLocationReadWriteClient = _Class("PPLocationReadWriteClient")
PPLocationNamedEntities = _Class("PPLocationNamedEntities")
PPEventHighlight = _Class("PPEventHighlight")
PPCustomDonation = _Class("PPCustomDonation")
PPTopicMetadata = _Class("PPTopicMetadata")
PPLocationReadOnlyClient = _Class("PPLocationReadOnlyClient")
PPNotificationManager = _Class("PPNotificationManager")
PPNotificationManagerGuardedData = _Class("PPNotificationManagerGuardedData")
PPNotificationHandler = _Class("PPNotificationHandler")
PPNotificationHandlerGuardedData = _Class("PPNotificationHandlerGuardedData")
PPNamedEntityReadOnlyClient = _Class("PPNamedEntityReadOnlyClient")
PPQuickTypeExplanationSet = _Class("PPQuickTypeExplanationSet")
PPScoredLocation = _Class("PPScoredLocation")
PPNamedEntityReadWriteClient = _Class("PPNamedEntityReadWriteClient")
PPReranker = _Class("PPReranker")
PPRerankerGuardedData = _Class("PPRerankerGuardedData")
PPConnectionsCriteria = _Class("PPConnectionsCriteria")
PPConnectionsClient = _Class("PPConnectionsClient")
PPContactClient = _Class("PPContactClient")
PPQuickTypeItem = _Class("PPQuickTypeItem")
PPRecordLoadingDelegate = _Class("PPRecordLoadingDelegate")
PPNamedEntityRecordLoadingDelegate = _Class("PPNamedEntityRecordLoadingDelegate")
PPEventNameRecordLoadingDelegate = _Class("PPEventNameRecordLoadingDelegate")
PPContactNameRecordLoadingDelegate = _Class("PPContactNameRecordLoadingDelegate")
PPXPCClientPipelinedBatchQueryManager = _Class("PPXPCClientPipelinedBatchQueryManager")
PPXPCClientPipelinedBatchQueryContext = _Class("PPXPCClientPipelinedBatchQueryContext")
PPXPCClientHelper = _Class("PPXPCClientHelper")
PPEventQuery = _Class("PPEventQuery")
PPTripEventQuery = _Class("PPTripEventQuery")
PPHighlightedEventQuery = _Class("PPHighlightedEventQuery")
PPSuggestedEventQuery = _Class("PPSuggestedEventQuery")
PPEventStore = _Class("PPEventStore")
PPTopicReadOnlyClient = _Class("PPTopicReadOnlyClient")
PPEnumTypes = _Class("PPEnumTypes")
PPLocationRecord = _Class("PPLocationRecord")
PPMutableLocationRecord = _Class("PPMutableLocationRecord")
PPLocation = _Class("PPLocation")
PPConfigClient = _Class("PPConfigClient")
PPSentimentScoreEncoder = _Class("PPSentimentScoreEncoder")
PPRecordMonitoringHelper = _Class("PPRecordMonitoringHelper")
PPBaseFeedback = _Class("PPBaseFeedback")
PPMappedFeedback = _Class("PPMappedFeedback")
PPFeedback = _Class("PPFeedback")
PPContactStore = _Class("PPContactStore")
PPEventNameRecord = _Class("PPEventNameRecord")
PPSiriQueryResult = _Class("PPSiriQueryResult")
PPUtils = _Class("PPUtils")
PPContactNameRecordChangeResult = _Class("PPContactNameRecordChangeResult")
PPTopicQuery = _Class("PPTopicQuery")
PPConnectionsLocation = _Class("PPConnectionsLocation")
PPTopicStore = _Class("PPTopicStore")
PPXPCTopicStore = _Class("PPXPCTopicStore")
PPLabeledValue = _Class("PPLabeledValue")
PPEvent = _Class("PPEvent")
PPAttendee = _Class("PPAttendee")
PPNamedEntityStore = _Class("PPNamedEntityStore")
PPXPCNamedEntityStore = _Class("PPXPCNamedEntityStore")
PPConstants = _Class("PPConstants")
PPScoredContact = _Class("PPScoredContact")
PPScoredLabeledValue = _Class("PPScoredLabeledValue")
PPLocationStore = _Class("PPLocationStore")
PPLocationQuery = _Class("PPLocationQuery")
PPCalendar = _Class("PPCalendar")
PPCalendarInternPool = _Class("PPCalendarInternPool")
PPTopicReadWriteClient = _Class("PPTopicReadWriteClient")
PPEventClient = _Class("PPEventClient")
PPInternalClient = _Class("PPInternalClient")
PPQuickTypeBroker = _Class("PPQuickTypeBroker")
PPQuickTypeQuery = _Class("PPQuickTypeQuery")
PPExtractionSet = _Class("PPExtractionSet")
PPClientFeedbackHelper = _Class("PPClientFeedbackHelper")
PPSource = _Class("PPSource")
PPScoredItem = _Class("PPScoredItem")
PPNamedEntityMetadata = _Class("PPNamedEntityMetadata")
PPNamedEntityRecord = _Class("PPNamedEntityRecord")
PPMutableNamedEntityRecord = _Class("PPMutableNamedEntityRecord")
PPNamedEntity = _Class("PPNamedEntity")
PPNamedEntityWithRecord = _Class("PPNamedEntityWithRecord")
PPSourceMetadata = _Class("PPSourceMetadata")