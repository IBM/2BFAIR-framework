import { NgModule } from '@angular/core';

import {
  ButtonModule,
  CheckboxModule,
  ContentSwitcherModule,
  DropdownModule,
  IconModule,
  IconService,
  InlineLoadingModule,
  InputModule,
  ModalModule,
  NumberModule,
  ProgressIndicatorModule,
  RadioModule,
  SelectModule,
  SliderModule,
  TableModule,
  TagModule,
  TilesModule,
  ToggleModule,
} from 'carbon-components-angular';

const carbonModules = [
  ButtonModule,
  CheckboxModule,
  ContentSwitcherModule,
  DropdownModule,
  IconModule,
  InputModule,
  InlineLoadingModule,
  ModalModule,
  ProgressIndicatorModule,
  SliderModule,
  NumberModule,
  ProgressIndicatorModule,
  RadioModule,
  SelectModule,
  SliderModule,
  TableModule,
  TagModule,
  TilesModule,
  ToggleModule,
];

@NgModule({
  imports: carbonModules,
  exports: carbonModules,
})
export class CarbonModule {}
