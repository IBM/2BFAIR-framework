// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Component, inject } from '@angular/core';

import { ExplorerComponent as LibExplorerComponent } from '@dwb/to-be-fair';

@Component({
  selector: 'app-explorer',
  standalone: true,
  imports: [LibExplorerComponent],
  templateUrl: './explorer.component.html',
  styleUrl: './explorer.component.css',
})
export class ExplorerComponent {}
