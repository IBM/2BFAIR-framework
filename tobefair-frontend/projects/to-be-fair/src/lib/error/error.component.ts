import { Component, Input } from '@angular/core';
import { CarbonModule } from '../carbon/carbon.module';
import { DataError32 } from '@carbon/icons';
import { IconService } from 'carbon-components-angular';

@Component({
  selector: 'lib-error',
  standalone: true,
  imports: [CarbonModule],
  templateUrl: './error.component.html',
  styleUrl: './error.component.css',
})
export class ErrorComponent {
  @Input() error: string | undefined;

  constructor(iconService: IconService) {
    iconService.registerAll([DataError32]);
  }
}
