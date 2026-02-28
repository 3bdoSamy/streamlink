# This module will get replaced by versioningit when building a source distribution
# and instead of trying to get the version string from git, a static version string will be set

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


def _get_version() -> str:
    """
    Get the current version with safe fallbacks.
    """

    # Prefer installed package metadata in regular and editable installs
    for package_name in ("streamlink-ar", "streamlink"):
        try:
            return version(package_name)
        except PackageNotFoundError:
            pass

    # Fall back to git-based version discovery when running directly from source
    try:
        from versioningit import get_version  # noqa: PLC0415
        import streamlink  # noqa: PLC0415

        return get_version(project_dir=Path(streamlink.__file__).parents[2])
    except Exception:
        return "0.0.0+unknown"


__version__ = _get_version()
