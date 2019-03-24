# This file is generated by objective.metadata
#
# Last update: Wed Jun  6 12:07:10 2018

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$UNNotificationAttachmentOptionsThumbnailClippingRectKey$UNNotificationAttachmentOptionsThumbnailHiddenKey$UNNotificationAttachmentOptionsThumbnailTimeKey$UNNotificationAttachmentOptionsTypeHintKey$UNNotificationDefaultActionIdentifier$UNNotificationDismissActionIdentifier$'''
enums = '''$UNAlertStyleAlert@2$UNAlertStyleBanner@1$UNAlertStyleNone@0$UNAuthorizationOptionAlert@4$UNAuthorizationOptionBadge@1$UNAuthorizationOptionCarPlay@8$UNAuthorizationOptionCriticalAlert@16$UNAuthorizationOptionNone@0$UNAuthorizationOptionProvidesAppNotificationSettings@32$UNAuthorizationOptionProvisional@64$UNAuthorizationOptionSound@2$UNAuthorizationStatusAuthorized@2$UNAuthorizationStatusDenied@1$UNAuthorizationStatusNotDetermined@0$UNAuthorizationStatusProvisional@3$UNErrorCodeAttachmentCorrupt@105$UNErrorCodeAttachmentInvalidFileSize@102$UNErrorCodeAttachmentInvalidURL@100$UNErrorCodeAttachmentMoveIntoDataStoreFailed@104$UNErrorCodeAttachmentNotInDataStore@103$UNErrorCodeAttachmentUnrecognizedType@101$UNErrorCodeNotificationInvalidNoContent@1401$UNErrorCodeNotificationInvalidNoDate@1400$UNErrorCodeNotificationsNotAllowed@1$UNNotificationActionOptionAuthenticationRequired@1$UNNotificationActionOptionDestructive@2$UNNotificationActionOptionForeground@4$UNNotificationActionOptionNone@0$UNNotificationCategoryOptionAllowInCarPlay@2$UNNotificationCategoryOptionCustomDismissAction@1$UNNotificationCategoryOptionHiddenPreviewsShowSubtitle@8$UNNotificationCategoryOptionHiddenPreviewsShowTitle@4$UNNotificationCategoryOptionNone@0$UNNotificationPresentationOptionAlert@4$UNNotificationPresentationOptionBadge@1$UNNotificationPresentationOptionNone@0$UNNotificationPresentationOptionSound@2$UNNotificationSettingDisabled@1$UNNotificationSettingEnabled@2$UNNotificationSettingNotSupported@0$UNShowPreviewsSettingAlways@0$UNShowPreviewsSettingNever@2$UNShowPreviewsSettingWhenAuthenticated@1$'''
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NSObject', b'userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:', {'arguments': {4: {'type': b'@?', 'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NSObject', b'userNotificationCenter:willPresentNotification:withCompletionHandler:', {'arguments': {4: {'type': b'@?', 'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Q'}}}}}})
    r(b'UNCalendarNotificationTrigger', b'triggerWithDateMatchingComponents:repeats:', {'arguments': {3: {'type': 'Z'}}})
    r(b'UNLocationNotificationTrigger', b'triggerWithRegion:repeats:', {'arguments': {3: {'type': 'Z'}}})
    r(b'UNNotificationAttachment', b'attachmentWithIdentifier:URL:options:error:', {'arguments': {5: {'type_modifier': b'o'}}})
    r(b'UNNotificationServiceExtension', b'didReceiveNotificationRequest:withContentHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'UNNotificationSettings', b'providesAppNotificationSettings', {'retval': {'type': 'Z'}})
    r(b'UNNotificationTrigger', b'repeats', {'retval': {'type': 'Z'}})
    r(b'UNTimeIntervalNotificationTrigger', b'triggerWithTimeInterval:repeats:', {'arguments': {3: {'type': 'Z'}}})
    r(b'UNUserNotificationCenter', b'addNotificationRequest:withCompletionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'UNUserNotificationCenter', b'getDeliveredNotificationsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'UNUserNotificationCenter', b'getNotificationCategoriesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'UNUserNotificationCenter', b'getNotificationSettingsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'UNUserNotificationCenter', b'getPendingNotificationRequestsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'UNUserNotificationCenter', b'requestAuthorizationWithOptions:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}, 2: {'type': b'@'}}}}}})
    r(b'UNUserNotificationCenter', b'supportsContentExtensions', {'retval': {'type': 'Z'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE