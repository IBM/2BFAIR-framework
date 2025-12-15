// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { HeaderModule, ThemeModule } from 'carbon-components-angular';

import { ResultComponent } from './result/result.component';
import { GlossaryComponent } from './glossary/glossary.component';
import { ExplorerComponent } from './explorer/explorer.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    RouterLink,
    RouterLinkActive,
    ResultComponent,
    GlossaryComponent,
    ExplorerComponent,
    HeaderModule,
    ThemeModule,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = '2BFAIR';
}
