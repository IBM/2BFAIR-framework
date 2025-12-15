import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'lib-tool-glossary',
  standalone: true,
  imports: [],
  templateUrl: './tool-glossary.component.html',
  styleUrl: './tool-glossary.component.css',
})
export class ToolGlossaryComponent {
  constructor(private route: ActivatedRoute) {}
  ngAfterViewInit(): void {
    this.route.fragment.subscribe((fragment: string | null) => {
      if (fragment) {
        setTimeout(() => {
          document
            .getElementById(fragment)
            ?.scrollIntoView({ behavior: 'smooth' });
        }, 0);
      }
    });
  }
}
