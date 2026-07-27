from __future__ import annotations

from models import (
    DownloadResult,
    ResourceInfo,
)


class SummaryService:

    @staticmethod
    def metadata(
        resource: ResourceInfo,
    ) -> dict:

        return {
            "title": resource.title,
            "uploader": resource.uploader,
            "duration": resource.duration,
            "type": resource.resource_type.value,
            "videos": resource.video_count,
        }

    @staticmethod
    def download(
        result: DownloadResult,
    ) -> dict:

        return {
            "success": result.success,
            "status": result.status.value,
            "output": (
                str(result.output_path)
                if result.output_path
                else None
            ),
            "error": result.error,
        }