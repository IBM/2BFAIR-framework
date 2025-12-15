// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component } from '@angular/core';
import { ResultReportComponent as LibResultReportComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'app-result-report',
  standalone: true,
  imports: [LibResultReportComponent],
  templateUrl: './result-report.component.html',
  styleUrl: './result-report.component.css',
})
export class ResultReportComponent {}
