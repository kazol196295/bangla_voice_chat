"""
Views for Voice Chat Application
"""

from django.shortcuts import render


def voice_chat_view(request):
    """Render the voice chat interface."""
    return render(
        request, "voice_chat/index.html", {"page_title": "বাংলা ভয়েস চ্যাট AI"}
    )


def health_check(request):
    """Health check endpoint."""
    from django.http import JsonResponse

    return JsonResponse({"status": "healthy"})


def clear_history(request):
    """Clear conversation history (for reset functionality)."""
    from django.http import JsonResponse

    # This would need WebSocket implementation to actually clear
    return JsonResponse({"status": "history_cleared"})
