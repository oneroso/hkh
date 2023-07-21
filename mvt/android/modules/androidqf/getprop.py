# Mobile Verification Toolkit (MVT)
# Copyright (c) 2021-2023 Claudio Guarnieri.
# Use of this software is governed by the MVT License 1.1 that can be found at
#   https://license.mvt.re/1.1/

import logging
from typing import Optional

from mvt.android.modules.detection_mixins import GetPropDetectionMixin
from mvt.android.parsers.getprop import parse_getprop

from .base import AndroidQFModule


class Getprop(GetPropDetectionMixin, AndroidQFModule):
    """This module extracts data from get properties."""

    def __init__(
        self,
        file_path: Optional[str] = None,
        target_path: Optional[str] = None,
        results_path: Optional[str] = None,
        module_options: Optional[dict] = None,
        log: logging.Logger = logging.getLogger(__name__),
        results: Optional[list] = None,
    ) -> None:
        super().__init__(
            file_path=file_path,
            target_path=target_path,
            results_path=results_path,
            module_options=module_options,
            log=log,
            results=results,
        )
        self.results = []

    def run(self) -> None:
        getprop_files = self._get_files_by_pattern("*/getprop.txt")
        if not getprop_files:
            self.log.info("getprop.txt file not found")
            return

        with open(getprop_files[0]) as f:
            data = f.read()

        self.results = parse_getprop(data)
        self.log.info("Extracted a total of %d properties", len(self.results))
