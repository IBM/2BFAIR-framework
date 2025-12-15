// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
