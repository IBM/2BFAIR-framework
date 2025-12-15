// Copyright (C) 2025 IBM Corp.
// SPDX-License-Identifier: Apache-2.0

import { Routes } from '@angular/router';

import { EnvVarGuard } from '@dwb/to-be-fair';

import { ResultComponent } from './result/result.component';
import { GlossaryComponent } from './glossary/glossary.component';
import { ExplorerComponent } from './explorer/explorer.component';
import { DetailsComponent } from './details/details.component';
import { ToolGlossaryComponent } from './tool-glossary/tool-glossary.component';
import { UserGuideComponent } from './user-guide/user-guide.component';
import { ResultReportComponent } from './result-report/result-report.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  {
    path: '',
    canActivate: [EnvVarGuard],
    children: [
      {
        path: 'result',
        component: ResultComponent,
        title: 'Evaluation result',
      },
      {
        path: 'explorer',
        component: ExplorerComponent,
        title: 'Explore results',
      },
      {
        path: 'details',
        component: DetailsComponent,
        title: 'Detail results',
      },
      {
        path: 'glossary',
        component: GlossaryComponent,
        title: 'Glossary',
      },
      {
        path: 'tool-glossary',
        component: ToolGlossaryComponent,
        title: 'Tool Glossary',
      },
      {
        path: 'result-report',
        component: ResultReportComponent,
        title: 'Full Report',
      },
      {
        path: '',
        component: HomeComponent,
        title: 'Home',
      },
      {
        path: 'user-guide',
        component: UserGuideComponent,
        title: 'User Guide',
      },
      // {
      //   path: '**', component: PageNotFoundComponent,  // TODO: Wildcard route for a 404 page
      // },
    ],
  },
];
