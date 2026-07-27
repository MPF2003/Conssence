class YouTubeDownloaderError(Exception):
    """Base exception for the application."""


class DownloadError(YouTubeDownloaderError):
    """Raised when a download fails."""


class MetadataError(YouTubeDownloaderError):
    """Raised when metadata extraction fails."""


class AuthenticationError(YouTubeDownloaderError):
    """Raised when YouTube authentication fails."""


class NetworkError(YouTubeDownloaderError):
    """Raised when a network error occurs."""


class InvalidURLError(YouTubeDownloaderError):
    """Raised when the provided URL is invalid."""


class InvalidResourceError(YouTubeDownloaderError):
    """Raised when the resource type is unsupported."""


class ConfigurationError(YouTubeDownloaderError):
    """Raised when the application configuration is invalid."""