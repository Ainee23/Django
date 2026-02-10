from django.db import models


# =========================
# USER MODEL
# =========================
class Test1User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)

    role = models.CharField(
        max_length=10,
        choices=[
            ('ADMIN', 'ADMIN'),
            ('USER', 'USER')
        ],
        default='USER'
    )

    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "test1_user"

    def __str__(self):
        return self.full_name


# =========================
# LOCATION
# =========================
class Location(models.Model):
    user = models.ForeignKey(
        Test1User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="locations"
    )
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "location"

    def __str__(self):
        return self.address
# =========================
# LOST ITEM (Owner role dynamically)
# =========================
class LostItem(models.Model):
    user = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="lost_items"
    )
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lost_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=[
            ('LOST', 'LOST'),
            ('MATCHED', 'MATCHED'),
            ('RECOVERED', 'RECOVERED')
        ],
        default='LOST'
    )

    ai_confidence_score = models.FloatField(null=True, blank=True)
    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "lost_item"

    def __str__(self):
        return self.item_name


# =========================
# FOUND ITEM (Finder role dynamically)
# =========================
class FoundItem(models.Model):
    user = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="found_items"
    )
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    found_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=[
            ('FOUND', 'FOUND'),
            ('CLAIMED', 'CLAIMED'),
            ('RETURNED', 'RETURNED')
        ],
        default='FOUND'
    )

    reported_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "found_item"

    def __str__(self):
        return self.item_name


# =========================
# QR CODE
# =========================
class QRCode(models.Model):
    linked_item = models.OneToOneField(LostItem, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "qr_code"


# =========================
# MESSAGE
# =========================
class Message(models.Model):
    sender = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    message_text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "message"


# =========================
# NOTIFICATION
# =========================
class Notification(models.Model):
    user = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    notification_type = models.CharField(
        max_length=20,
        choices=[
            ('MATCH_FOUND', 'MATCH_FOUND'),
            ('CLAIM_REQUEST', 'CLAIM_REQUEST'),
            ('ITEM_RETURNED', 'ITEM_RETURNED')
        ]
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notification"


# =========================
# RATING
# =========================
class Rating(models.Model):
    rated_user = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="ratings_received"
    )
    rated_by_user = models.ForeignKey(
        Test1User,
        on_delete=models.CASCADE,
        related_name="ratings_given"
    )
    item = models.ForeignKey(LostItem, on_delete=models.CASCADE)
    rating_value = models.IntegerField()
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "rating"


# =========================
# ADMIN LOG
# =========================
class AdminLog(models.Model):
    admin = models.ForeignKey(Test1User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    action_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "admin_log"
