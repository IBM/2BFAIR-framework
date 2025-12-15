import { Routes } from '@angular/router';

import { ResultComponent } from './result/result.component';
import { GlossaryComponent } from './glossary/glossary.component';
import { ExplorerComponent } from './explorer/explorer.component';
import { DetailsComponent } from './details/details.component';
import { ToolGlossaryComponent } from './tool-glossary/tool-glossary.component';
import { ResultReportComponent } from './result-report/result-report.component';

export const routes: Routes = [
  {
    path: 'result',
    component: ResultComponent,
    title: 'Evaluation Result',
  },
  {
    path: 'explorer',
    component: ExplorerComponent,
    title: 'Explore Results',
  },
  {
    path: 'details',
    component: DetailsComponent,
    title: 'Detail Results',
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
  // {
  //   path: '**', component: PageNotFoundComponent,  // TODO: Wildcard route for a 404 page
  // },
];
